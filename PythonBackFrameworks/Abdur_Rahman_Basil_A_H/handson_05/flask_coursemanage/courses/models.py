from extensions import db

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    courses = db.relationship('Course', back_populates='department')

    def to_dict(self):
        return {"id": self.id, "name": self.name}

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    department = db.relationship('Department', back_populates='courses')
    enrollments = db.relationship('Enrollment', back_populates='course', cascade='all, delete-orphan')

    def __init__(self, name, code, credits, department_id, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.code = code
        self.credits = credits
        self.department_id = department_id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "credits": self.credits,
            "department_id": self.department_id
        }

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    enrollments = db.relationship('Enrollment', back_populates='student', cascade='all, delete-orphan')

    def to_dict(self):
        return {"id": self.id, "name": self.name}

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(2))
    
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    
    student = db.relationship('Student', back_populates='enrollments')
    course = db.relationship('Course', back_populates='enrollments')

    def __init__(self, student_id, course_id, grade=None, **kwargs):
        super().__init__(**kwargs)
        self.student_id = student_id
        self.course_id = course_id
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.id,
            "grade": self.grade,
            "student_id": self.student_id,
            "course_id": self.course_id
        }