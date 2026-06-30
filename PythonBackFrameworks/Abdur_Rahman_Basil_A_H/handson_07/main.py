from fastapi import FastAPI, Depends,HTTPException,status,BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from contextlib import asynccontextmanager
from typing import Optional,List
from schemas import CourseCreate,CourseResponse
from database import engine, Base, get_db
import models 
from schemas import CourseUpdate

from schemas import (
    CourseCreate, CourseResponse, CourseUpdate,
    StudentCreate, StudentResponse,          
    EnrollmentCreate, EnrollmentResponse     
)

# tells fastapi to create db tables on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title='Digital Nurture Course Management API',
    description='A fully async RESTful API for managing studnets, courses, and enrollments.',
    version='1.0.0',
    contact={
        "name": "API Support Team",
        "email": "support@example.com",
    },
    lifespan=lifespan
)

def send_confirmation_email(student_email: str):
    print(f'----- [BACKGROUND TASK] Sending confirmation to {student_email} -----')

@app.get("/")
def root():
    """check if API is runing"""
    return {'message':'API running'}

@app.post('/api/courses/', response_model=CourseResponse,status_code=status.HTTP_201_CREATED,tags=["Courses"])
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    """create a new course"""
    # inject db session and convert schema to db model
    db_course = models.Course(**course.model_dump()) 
    
    # add and commit to db
    db.add(db_course)
    await db.commit()
    
    # refresh to get new id
    await db.refresh(db_course)
    
    # return the db course instance
    return db_course

@app.get('/api/courses/{course_id}', response_model=CourseResponse,tags=["Courses"])
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    """get course by id"""
    # query course by id
    query = select(models.Course).where(models.Course.id == course_id)
    result = await db.execute(query)
    
    # fetch single record or none
    course = result.scalar_one_or_none()
    
    # raise 404 if course not found
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
        
    return course

@app.get('/api/courses/', response_model=List[CourseResponse],tags=["Courses"])
async def get_courses(
    skip: int = 0, 
    limit: int = 10, 
    department_id: Optional[int] = None, 
    db: AsyncSession = Depends(get_db)
):
    """get all courses with paginaton"""
    # base query for courses
    query = select(models.Course)
    
    # filter by department if provided
    if department_id is not None:
        query = query.where(models.Course.department_id == department_id)
        
    # apply limit and skip offsets
    query = query.offset(skip).limit(limit)
    
    result = await db.execute(query)
    
    # get all course results as list
    courses = result.scalars().all()
    return courses

@app.put('/api/courses/{course_id}', response_model=CourseResponse,status_code=status.HTTP_200_OK,tags=["Courses"])
async def update_course(course_id: int, course_update: CourseUpdate, db: AsyncSession = Depends(get_db)):
    """updaet an existing course"""
    # find existing course
    query = select(models.Course).where(models.Course.id == course_id)
    result = await db.execute(query)
    db_course = result.scalar_one_or_none()
    
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
        
    # get only fields that are set
    update_data = course_update.model_dump(exclude_unset=True)
    
    # apply changes to db object
    for key, value in update_data.items():
        setattr(db_course, key, value)
        
    # save and refresh course
    await db.commit()
    await db.refresh(db_course)
    return db_course

@app.delete('/api/courses/{course_id}',status_code=status.HTTP_204_NO_CONTENT,tags=["Courses"])
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)):
    """delete a course by ID"""
    # find existing course
    query = select(models.Course).where(models.Course.id == course_id)
    result = await db.execute(query)
    db_course = result.scalar_one_or_none()
    
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
        
    # delete and commit
    await db.delete(db_course)
    await db.commit()
    
    return {"message": f"Course {course_id} deleted successfully"}

@app.post('/api/students/', response_model=StudentResponse, status_code=status.HTTP_201_CREATED,tags=["Student"])
async def create_student(student: StudentCreate, db: AsyncSession = Depends(get_db)):
    """create a new studnet"""
    # create student record
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    await db.commit()
    await db.refresh(db_student)
    return db_student

@app.post('/api/enrollments/', response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED,tags=["Enrollment"])
async def create_enrollment(
    enrollment: EnrollmentCreate, 
    background_tasks: BackgroundTasks,  # background tasks
    db: AsyncSession = Depends(get_db)
):
    """enroll a studnet to a course"""
    # insert enrollment record
    db_enrollment = models.Enrollment(**enrollment.model_dump())
    db.add(db_enrollment)
    await db.commit()
    await db.refresh(db_enrollment)
    
    # get student email
    student_query = select(models.Student).where(models.Student.id == enrollment.student_id)
    result = await db.execute(student_query)
    student = result.scalar_one_or_none()
    
    # add confirmation email task to background
    if student:
        background_tasks.add_task(send_confirmation_email, student.email)
        
    # return enrollment immediately while background task runs
    return db_enrollment

@app.get('/api/courses/{course_id}/students/', response_model=List[StudentResponse],tags=["Student"])
async def get_course_students(course_id: int, db: AsyncSession = Depends(get_db)):
    """get all studnets enrolled in a course"""
    # query students joined with enrollments
    query = (
        select(models.Student)
        .join(models.Enrollment)
        .where(models.Enrollment.course_id == course_id)
    )
    
    result = await db.execute(query)
    students = result.scalars().all() 
    
    return students

@app.get('/api/students/', response_model=List[StudentResponse], status_code=status.HTTP_200_OK,tags=["Student"])
async def get_students(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    """get all registered studnets"""
    # query students with paginaton
    query = select(models.Student).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

@app.get('/api/students/{student_id}', response_model=StudentResponse, status_code=status.HTTP_200_OK,tags=["Student"])
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    """get single studnet by id"""
    # find student by id
    query = select(models.Student).where(models.Student.id == student_id)
    result = await db.execute(query)
    student = result.scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student

@app.put('/api/students/{student_id}', response_model=StudentResponse, status_code=status.HTTP_200_OK,tags=["Student"])
async def update_student(student_id: int, student_update: StudentCreate, db: AsyncSession = Depends(get_db)):
    """update a studnet record"""
    # find and update student details
    query = select(models.Student).where(models.Student.id == student_id)
    result = await db.execute(query)
    db_student = result.scalar_one_or_none()
    
    if not db_student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
        
    update_data = student_update.model_dump()
    for key, value in update_data.items():
        setattr(db_student, key, value)
        
    await db.commit()
    await db.refresh(db_student)
    return db_student

@app.delete('/api/students/{student_id}', status_code=status.HTTP_204_NO_CONTENT,tags=["Student"])
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):
    """delete a studnet"""
    # find and delete student
    query = select(models.Student).where(models.Student.id == student_id)
    result = await db.execute(query)
    db_student = result.scalar_one_or_none()
    
    if not db_student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
        
    await db.delete(db_student)
    await db.commit()

@app.get('/api/enrollments/', response_model=List[EnrollmentResponse], status_code=status.HTTP_200_OK,tags=["Enrollment"])
async def get_enrollments(db: AsyncSession = Depends(get_db)):
    """get all enrollmnts"""
    # query enrollments
    query = select(models.Enrollment)
    result = await db.execute(query)
    return result.scalars().all()

@app.delete('/api/enrollments/{enrollment_id}', status_code=status.HTTP_204_NO_CONTENT,tags=["Enrollment"])
async def delete_enrollment(enrollment_id: int, db: AsyncSession = Depends(get_db)):
    """cancel an enrollmnt"""
    # find and delete enrollment
    query = select(models.Enrollment).where(models.Enrollment.id == enrollment_id)
    result = await db.execute(query)
    db_enrollment = result.scalar_one_or_none()
    
    if not db_enrollment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enrollment not found")
        
    await db.delete(db_enrollment)
    await db.commit()