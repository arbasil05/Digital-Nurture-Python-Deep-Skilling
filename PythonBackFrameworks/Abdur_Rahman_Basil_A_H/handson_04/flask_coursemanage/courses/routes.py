from flask import Blueprint, jsonify, request
from app import db
from courses.

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

# --- HELPER FUNCTION ---
def make_response_json(data, status_code=200):
    return jsonify({'status': 'success', 'data': data}), status_code

# --- ROUTES ---

@courses_bp.route('/', methods=['GET'])
def get_all_courses():
    # 52: Query all courses and serialize them
    courses = Course.query.all()
    return make_response_json([course.to_dict() for course in courses], 200)


@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error', 'message': 'Invalid JSON'}), 400
        
    # We now require department_id since the DB strictly requires it
    required_fields = ['name', 'code', 'credits', 'department_id']
    for field in required_fields:
        if field not in data:
            return jsonify({'status': 'error', 'message': f'Missing: {field}'}), 400
            
    # 54: Create ORM object, add to session, and commit
    new_course = Course(
        name=data['name'],
        code=data['code'],
        credits=data['credits'],
        department_id=data['department_id']
    )
    db.session.add(new_course)
    db.session.commit()
    
    return make_response_json(new_course.to_dict(), 201)


@courses_bp.route('/<int:course_id>', methods=['GET'])
def get_course(course_id):
    # 55: get_or_404 automatically returns a 404 error if not found
    course = db.get_or_404(Course, course_id)
    return make_response_json(course.to_dict(), 200)


@courses_bp.route('/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    course = db.get_or_404(Course, course_id)
    data = request.get_json()
    
    if 'name' in data: course.name = data['name']
    if 'code' in data: course.code = data['code']
    if 'credits' in data: course.credits = data['credits']
    if 'department_id' in data: course.department_id = data['department_id']
    
    db.session.commit()
    return make_response_json(course.to_dict(), 200)


@courses_bp.route('/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = db.get_or_404(Course, course_id)
    
    db.session.delete(course)
    db.session.commit()
    
    return make_response_json({'message': f'Course {course_id} deleted'}, 200)


@courses_bp.route('/<int:course_id>/students/', methods=['GET'])
def get_course_students(course_id):
    # 56: JOIN Query to get all students enrolled in a specific course
    course = db.get_or_404(Course, course_id)
    
    # This joins the Student table with the Enrollment table where the course_id matches
    students = db.session.query(Student)\
        .join(Enrollment)\
        .filter(Enrollment.course_id == course_id)\
        .all()
        
    return make_response_json([student.to_dict() for student in students], 200)