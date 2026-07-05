from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks, Response, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func, or_
from contextlib import asynccontextmanager
from typing import Optional, List
from urllib.parse import urlencode

from database import engine, Base, get_db
import models
from schemas import (
    CourseCreate, CourseResponse, CourseUpdate, CoursePaginatedResponse,
    StudentCreate, StudentUpdate, StudentResponse,
    EnrollmentCreate, EnrollmentResponse
)

"""
--- API VERSIONING STRATEGY DISCUSSION ---
1. URL Versioning (e.g., /api/v1/courses/):
   - Pros: Simple to implement, highly visible, easy to test directly in a web browser, and makes routing straightforward.
   - Cons: Violates URI stability since version changes alter the resource identifier path.

2. Header-based Versioning (e.g., Accept: application/vnd.api+json;version=1 or X-API-Version: 1):
   - Pros: Keeps URLs clean, adheres to resource-centric REST principles (a URI represents the resource itself, and media types define representation version).
   - Cons: Harder to test directly in a web browser without plugins, adds complexity to routing logic and caching servers.
"""

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title='Digital Nurture Course Management API (REST Best Practices Refactored)',
    description='A fully async RESTful API for managing students, courses, and enrollments, refactored according to RESTful API Design Best Practices.',
    version='1.0.0',
    lifespan=lifespan
)

# Custom Exception Handlers to Standardise Error Responses
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    status_to_code = {
        400: "BAD_REQUEST",
        401: "UNAUTHORIZED",
        403: "FORBIDDEN",
        404: "NOT_FOUND",
        409: "CONFLICT",
        422: "UNPROCESSABLE_ENTITY",
        500: "INTERNAL_SERVER_ERROR"
    }
    code = status_to_code.get(exc.status_code, "ERROR")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": code,
                "message": exc.detail,
                "field": None
            }
        }
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    message = "Request validation failed"
    field = None
    if errors:
        err = errors[0]
        loc = err.get("loc", [])
        # Extract the field location from the tuple (usually begins with body, query, etc.)
        field = ".".join(str(l) for l in loc[1:]) if len(loc) > 1 else str(loc[0]) if loc else None
        msg = err.get("msg")
        message = f"Field validation failed for '{field}': {msg}" if field else msg
        
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": {
                "code": "VALIDATION_ERROR",
                "message": message,
                "field": field
            }
        }
    )

def send_confirmation_email(student_email: str):
    print(f'----- [BACKGROUND TASK] Sending confirmation to {student_email} -----')

@app.get("/")
def root():
    """Check if API is running"""
    return {'message': 'API running'}

# --- COURSES ENDPOINTS ---

@app.post('/api/v1/courses/', response_model=CourseResponse, status_code=status.HTTP_201_CREATED, tags=["Courses"])
async def create_course(course: CourseCreate, response: Response, db: AsyncSession = Depends(get_db)):
    """Create a new course"""
    db_course = models.Course(**course.model_dump())
    db.add(db_course)
    await db.commit()
    await db.refresh(db_course)
    
    # Set Location response header
    response.headers['Location'] = f'/api/v1/courses/{db_course.id}'
    return db_course

@app.get('/api/v1/courses/{course_id}', response_model=CourseResponse, tags=["Courses"])
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    """Get course by ID"""
    query = select(models.Course).where(models.Course.id == course_id)
    result = await db.execute(query)
    course = result.scalar_one_or_none()
    
    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Course with id {course_id} does not exist"
        )
        
    return course

@app.get('/api/v1/courses/', response_model=CoursePaginatedResponse, tags=["Courses"])
async def get_courses(
    request: Request,
    page: int = 1,
    page_size: int = 10,
    search: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """Get all courses with pagination and filtering"""
    if page < 1:
        raise HTTPException(status_code=400, detail="Page must be greater than or equal to 1")
    if page_size < 1:
        raise HTTPException(status_code=400, detail="Page size must be greater than or equal to 1")

    # Base query
    query = select(models.Course)
    count_query = select(func.count()).select_from(models.Course)

    # Search filter (case-insensitive LIKE on name and code)
    if search:
        search_filter = or_(
            models.Course.name.ilike(f"%{search}%"),
            models.Course.code.ilike(f"%{search}%")
        )
        query = query.where(search_filter)
        count_query = count_query.where(search_filter)

    # Execute count
    count_result = await db.execute(count_query)
    total = count_result.scalar()

    # Execute paginated results
    offset = (page - 1) * page_size
    query = query.offset(offset).limit(page_size)
    result = await db.execute(query)
    courses = result.scalars().all()

    # Construct pagination links
    base_url = str(request.url).split('?')[0]

    next_url = None
    if offset + page_size < total:
        params = dict(request.query_params)
        params['page'] = page + 1
        params['page_size'] = page_size
        next_url = f"{base_url}?{urlencode(params)}"

    prev_url = None
    if page > 1:
        params = dict(request.query_params)
        params['page'] = page - 1
        params['page_size'] = page_size
        prev_url = f"{base_url}?{urlencode(params)}"

    return {
        "count": total,
        "next": next_url,
        "previous": prev_url,
        "results": courses
    }

@app.put('/api/v1/courses/{course_id}', response_model=CourseResponse, tags=["Courses"])
async def replace_course(course_id: int, course_replace: CourseCreate, db: AsyncSession = Depends(get_db)):
    """Full update/replace of an existing course"""
    query = select(models.Course).where(models.Course.id == course_id)
    result = await db.execute(query)
    db_course = result.scalar_one_or_none()
    
    if db_course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Course with id {course_id} does not exist"
        )
        
    # Replace all fields (PUT semantics)
    replace_data = course_replace.model_dump()
    for key, value in replace_data.items():
        setattr(db_course, key, value)
        
    await db.commit()
    await db.refresh(db_course)
    return db_course

@app.patch('/api/v1/courses/{course_id}', response_model=CourseResponse, tags=["Courses"])
async def update_course(course_id: int, course_update: CourseUpdate, db: AsyncSession = Depends(get_db)):
    """Partial update of an existing course"""
    query = select(models.Course).where(models.Course.id == course_id)
    result = await db.execute(query)
    db_course = result.scalar_one_or_none()
    
    if db_course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Course with id {course_id} does not exist"
        )
        
    # Apply partial fields (PATCH semantics)
    update_data = course_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_course, key, value)
        
    await db.commit()
    await db.refresh(db_course)
    return db_course

@app.delete('/api/v1/courses/{course_id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Courses"])
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)):
    """Delete a course by ID"""
    query = select(models.Course).where(models.Course.id == course_id)
    result = await db.execute(query)
    db_course = result.scalar_one_or_none()
    
    if db_course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Course with id {course_id} does not exist"
        )
        
    await db.delete(db_course)
    await db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# --- STUDENTS ENDPOINTS ---

@app.post('/api/v1/students/', response_model=StudentResponse, status_code=status.HTTP_201_CREATED, tags=["Students"])
async def create_student(student: StudentCreate, response: Response, db: AsyncSession = Depends(get_db)):
    """Create a new student"""
    # Check if student with same email exists
    email_query = select(models.Student).where(models.Student.email == student.email)
    email_result = await db.execute(email_query)
    if email_result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Student with this email already exists"
        )

    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    await db.commit()
    await db.refresh(db_student)
    
    # Set Location response header
    response.headers['Location'] = f'/api/v1/students/{db_student.id}'
    return db_student

@app.get('/api/v1/students/', response_model=List[StudentResponse], tags=["Students"])
async def get_students(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    """Get registered students"""
    query = select(models.Student).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

@app.get('/api/v1/students/{student_id}', response_model=StudentResponse, tags=["Students"])
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    """Get single student by ID"""
    query = select(models.Student).where(models.Student.id == student_id)
    result = await db.execute(query)
    student = result.scalar_one_or_none()
    
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Student with id {student_id} does not exist"
        )
        
    return student

@app.put('/api/v1/students/{student_id}', response_model=StudentResponse, tags=["Students"])
async def replace_student(student_id: int, student_replace: StudentCreate, db: AsyncSession = Depends(get_db)):
    """Full update/replace of student details"""
    query = select(models.Student).where(models.Student.id == student_id)
    result = await db.execute(query)
    db_student = result.scalar_one_or_none()
    
    if db_student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Student with id {student_id} does not exist"
        )
        
    replace_data = student_replace.model_dump()
    for key, value in replace_data.items():
        setattr(db_student, key, value)
        
    await db.commit()
    await db.refresh(db_student)
    return db_student

@app.patch('/api/v1/students/{student_id}', response_model=StudentResponse, tags=["Students"])
async def update_student(student_id: int, student_update: StudentUpdate, db: AsyncSession = Depends(get_db)):
    """Partial update of student details"""
    query = select(models.Student).where(models.Student.id == student_id)
    result = await db.execute(query)
    db_student = result.scalar_one_or_none()
    
    if db_student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Student with id {student_id} does not exist"
        )
        
    update_data = student_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_student, key, value)
        
    await db.commit()
    await db.refresh(db_student)
    return db_student

@app.delete('/api/v1/students/{student_id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Students"])
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):
    """Delete a student by ID"""
    query = select(models.Student).where(models.Student.id == student_id)
    result = await db.execute(query)
    db_student = result.scalar_one_or_none()
    
    if db_student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Student with id {student_id} does not exist"
        )
        
    await db.delete(db_student)
    await db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# --- ENROLLMENTS ENDPOINTS ---

@app.post('/api/v1/enrollments/', response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED, tags=["Enrollments"])
async def create_enrollment(
    enrollment: EnrollmentCreate, 
    background_tasks: BackgroundTasks, 
    response: Response,
    db: AsyncSession = Depends(get_db)
):
    """Enroll a student to a course"""
    # Verify student exists
    student_query = select(models.Student).where(models.Student.id == enrollment.student_id)
    student_result = await db.execute(student_query)
    student = student_result.scalar_one_or_none()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Student with id {enrollment.student_id} does not exist"
        )

    # Verify course exists
    course_query = select(models.Course).where(models.Course.id == enrollment.course_id)
    course_result = await db.execute(course_query)
    course = course_result.scalar_one_or_none()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Course with id {enrollment.course_id} does not exist"
        )

    # Verify not already enrolled
    existing_query = select(models.Enrollment).where(
        models.Enrollment.student_id == enrollment.student_id,
        models.Enrollment.course_id == enrollment.course_id
    )
    existing_result = await db.execute(existing_query)
    if existing_result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Student is already enrolled in this course"
        )

    db_enrollment = models.Enrollment(**enrollment.model_dump())
    db.add(db_enrollment)
    await db.commit()
    await db.refresh(db_enrollment)
    
    # Send email task in the background
    background_tasks.add_task(send_confirmation_email, student.email)
    
    # Set Location response header
    response.headers['Location'] = f'/api/v1/enrollments/{db_enrollment.id}'
    return db_enrollment

@app.get('/api/v1/enrollments/', response_model=List[EnrollmentResponse], tags=["Enrollments"])
async def get_enrollments(db: AsyncSession = Depends(get_db)):
    """Get all enrollments"""
    query = select(models.Enrollment)
    result = await db.execute(query)
    return result.scalars().all()

@app.delete('/api/v1/enrollments/{enrollment_id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Enrollments"])
async def delete_enrollment(enrollment_id: int, db: AsyncSession = Depends(get_db)):
    """Cancel/delete an enrollment"""
    query = select(models.Enrollment).where(models.Enrollment.id == enrollment_id)
    result = await db.execute(query)
    db_enrollment = result.scalar_one_or_none()
    
    if db_enrollment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Enrollment with id {enrollment_id} does not exist"
        )
        
    await db.delete(db_enrollment)
    await db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get('/api/v1/courses/{course_id}/students/', response_model=List[StudentResponse], tags=["Students"])
async def get_course_students(course_id: int, db: AsyncSession = Depends(get_db)):
    """Get all students enrolled in a course"""
    # Verify course exists
    course_query = select(models.Course).where(models.Course.id == course_id)
    course_result = await db.execute(course_query)
    if course_result.scalar_one_or_none() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Course with id {course_id} does not exist"
        )

    query = (
        select(models.Student)
        .join(models.Enrollment)
        .where(models.Enrollment.course_id == course_id)
    )
    result = await db.execute(query)
    return result.scalars().all()
