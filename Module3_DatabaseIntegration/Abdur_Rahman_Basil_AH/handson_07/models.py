from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    student_id = Column(Integer,primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    enrollment_year = Column(Integer)
    is_active = Column(Boolean,default=True)

class Course(Base):
    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(100))
    course_code = Column(String(20))

class CourseSchedule(Base):
    __tablename__ = 'course_schedules'

    schedule_id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.course_id'))
    day_of_week = Column(String(15))
    start_time = Column(String(10)) 
    end_time = Column(String(10))
