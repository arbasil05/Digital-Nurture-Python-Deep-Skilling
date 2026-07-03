from sqlalchemy.orm import sessionmaker,joinedload
from models import Base, engine, Student, Department, Enrollment, Course


print("Re-creating tables...")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

print("\n--- Step 81: INSERT Departments and Students ---")

dept_cs = Department(dept_name='Computer Science')
dept_math = Department(dept_name='Mathematics')
dept_physics = Department(dept_name='Physics')

session.add_all([dept_cs, dept_math, dept_physics])
session.commit()

student_alice = Student(first_name='Alice', last_name='Smith', email='alice@example.com', enrollment_year=2024, department=dept_cs)
student_bob = Student(first_name='Bob', last_name='Jones', email='bob@example.com', enrollment_year=2023, department=dept_cs)
student_charlie = Student(first_name='Charlie', last_name='Brown', email='charlie@example.com', enrollment_year=2024, department=dept_math)
student_diana = Student(first_name='Diana', last_name='Prince', email='diana@example.com', enrollment_year=2022, department=dept_physics)
student_evan = Student(first_name='Evan', last_name='Wright', email='evan@example.com', enrollment_year=2023, department=dept_cs)

session.add_all([student_alice, student_bob, student_charlie, student_diana, student_evan])
session.commit()
print("Departments and Students inserted successfully!")

print("\n--- Step 82: INSERT Courses and Enrollments ---")

course_db = Course(title='Database Systems', credits=4)
course_algo = Course(title='Algorithms', credits=4)
course_calc = Course(title='Calculus', credits=3)

session.add_all([course_db, course_algo, course_calc])
session.commit()


enrollment_1 = Enrollment(student=student_alice, course=course_db, grade=3.50)
enrollment_2 = Enrollment(student=student_bob, course=course_db, grade=3.80)
enrollment_3 = Enrollment(student=student_charlie, course=course_calc, grade=3.90)
enrollment_4 = Enrollment(student=student_evan, course=course_algo, grade=4.00)

session.add_all([enrollment_1, enrollment_2, enrollment_3, enrollment_4])
session.commit()
print("Courses and Enrollments inserted successfully!")

print("\n--- Step 83: READ Query Students in 'Computer Science' ---")

cs_students = session.query(Student).join(Department).filter(Department.dept_name == 'Computer Science').all()
print("Students in Computer Science:")
for s in cs_students:
    print(f"- {s.first_name} {s.last_name} (Email: {s.email}, Year: {s.enrollment_year})")

print("\n--- Step 84: READ Query All Enrollments (Observing N+1 Problem) ---")
enrollments = session.query(Enrollment).all()
print(f"Total enrollments found: {len(enrollments)}")
for e in enrollments:
    print(f"Enrollment Record: Student: {e.student.first_name} {e.student.last_name} | Course: {e.course.title} | Grade: {e.grade}")

print("\n--- Step 85: UPDATE Find student by email and update enrollment_year ---")

student_to_update = session.query(Student).filter(Student.email == 'bob@example.com').first()
if student_to_update:
    print(f"Found student: {student_to_update.first_name} {student_to_update.last_name}, current enrollment year: {student_to_update.enrollment_year}")
    student_to_update.enrollment_year = 2025
    session.commit()
    print("Student enrollment year updated and committed!")

print("\n--- Step 86: DELETE Remove an enrollment record ---")

enrollment_to_delete = session.query(Enrollment).filter(Enrollment.student_id == student_alice.id, Enrollment.course_id == course_db.id).first()
if enrollment_to_delete:
    print(f"Deleting enrollment for {student_alice.first_name} in {course_db.title}...")
    session.delete(enrollment_to_delete)
    session.commit()
    print("Enrollment deleted and committed!")


remaining_enrollments = session.query(Enrollment).all()
print(f"Remaining enrollments count: {len(remaining_enrollments)}")
for re in remaining_enrollments:
    print(f"- Student ID: {re.student_id}, Course ID: {re.course_id}, Grade: {re.grade}")

"""
Hands-On 6 - N+1 Problem Documentation:
- Task 2 (Step 84) demonstrated the N+1 problem (Lazy Loading). Fetching enrollments caused 1 initial query, plus 2 extra queries (student and course) for EVERY enrollment record in the loop.
- Task 3 (Step 88) solved this using `joinedload` (Eager Loading). It compiled everything into exactly 1 query using SQL LEFT OUTER JOINs, preventing the extra database hits during the loop.
"""

print("\n--- Step 88 & 89: READ Query with joinedload (Eager Loading) ---")

optimized_enrollments = session.query(Enrollment).options(
    joinedload(Enrollment.student), 
    joinedload(Enrollment.course)
).all()

print(f"Total optimized enrollments found: {len(optimized_enrollments)}")
for e in optimized_enrollments:
    print(f"Optimized Record: Student: {e.student.first_name} {e.student.last_name} | Course: {e.course.title} | Grade: {e.grade}")

session.close()