from flask import Blueprint, jsonify, request
from extensions import db
from courses.models import Course, Student, Enrollment

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')


def make_response_json(data, status_code=200):
    return jsonify({'status': 'success', 'data': data}), status_code


# Get the full list of courses.
@courses_bp.route('/', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return make_response_json([c.to_dict() for c in courses], 200)


# Add a new course to the database.
@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()

    if not data:
        return jsonify({
            'status': 'error',
            'message': 'Invalid or missing JSON payload'
        }), 400

    required_fields = ['name', 'code', 'credits', 'department_id']

    for field in required_fields:
        if field not in data:
            return jsonify({
                'status': 'error',
                'message': f'Missing required field: {field}'
            }), 400

    new_course = Course(
        name=data['name'],
        code=data['code'],
        credits=data['credits'],
        department_id=data['department_id']
    )

    db.session.add(new_course)
    db.session.commit()

    return make_response_json(new_course.to_dict(), 201)


# Look up a course by its ID.
@courses_bp.route('/<int:id>', methods=['GET'])
def get_course(id):
    course = Course.query.get_or_404(id)
    return make_response_json(course.to_dict(), 200)


# Update only the fields sent in the request.
@courses_bp.route('/<int:id>', methods=['PUT'])
def update_course(id):
    course = Course.query.get_or_404(id)
    data = request.get_json()

    if not data:
        return jsonify({
            'status': 'error',
            'message': 'Invalid or missing JSON payload'
        }), 400

    course.name = data.get('name', course.name)
    course.code = data.get('code', course.code)
    course.credits = data.get('credits', course.credits)
    if 'department_id' in data:
        course.department_id = data['department_id']

    db.session.commit()

    return make_response_json(course.to_dict(), 200)


# Delete a course if it exists.
@courses_bp.route('/<int:id>', methods=['DELETE'])
def delete_course(id):
    course = Course.query.get_or_404(id)
    
    db.session.delete(course)
    db.session.commit()

    return make_response_json(
        {'message': f'Course {id} deleted'},
        200
    )


# Get all students enrolled in a course.
@courses_bp.route('/<int:id>/students/', methods=['GET'])
def get_course_students(id):
    # Verify the course exists
    Course.query.get_or_404(id)

    # Use JOIN query to fetch students enrolled in the specified course
    students = Student.query.join(Enrollment).filter(Enrollment.course_id == id).all()

    return make_response_json([s.to_dict() for s in students], 200)