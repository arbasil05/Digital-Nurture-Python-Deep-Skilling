import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship, declarative_base


load_dotenv()


db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")


DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(DATABASE_URI, echo=True)


Base = declarative_base()


class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    dept_name = Column(String(100), nullable=False)
    
    # Bidirectional relationship
    students = relationship('Student', back_populates='department')
    professors = relationship('Professor', back_populates='department')

class Professor(Base):
    __tablename__ = 'professors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'))
    
    department = relationship('Department', back_populates='professors')
    courses = relationship('Course', back_populates='professor')

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    enrollment_year = Column(Integer)
    department_id = Column(Integer, ForeignKey('departments.id'))
    
    department = relationship('Department', back_populates='students')
    enrollments = relationship('Enrollment', back_populates='student')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    credits = Column(Integer, nullable=False)
    professor_id = Column(Integer, ForeignKey('professors.id'))
    
    professor = relationship('Professor', back_populates='courses')
    enrollments = relationship('Enrollment', back_populates='course')

class Enrollment(Base):
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    grade = Column(Numeric(3, 2)) # e.g., 3.85
    
    student = relationship('Student', back_populates='enrollments')
    course = relationship('Course', back_populates='enrollments')

if __name__ == "__main__":
    print("Creating database tables...")
    Base.metadata.create_all(engine)
    print("Database tables created successfully!")


