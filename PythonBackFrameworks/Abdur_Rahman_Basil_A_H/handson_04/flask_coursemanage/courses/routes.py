from flask import Blueprint, jsonify, request

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

courses_db = []
course_id_counter = 1


def make_response_json(data, status_code=200):
    return jsonify({'status': 'success', 'data': data}), status_code


# Get the full list of courses.
@courses_bp.route('/', methods=['GET'])
def get_courses():
    return make_response_json(courses_db, 200)


# Add a new course to the in-memory database.
@courses_bp.route('/', methods=['POST'])
def create_course():

    global course_id_counter

    data = request.get_json()

    if not data:
        return jsonify({
            'status': 'error',
            'message': 'Invalid or missing JSON payload'
        }), 400

    required_fields = ['name', 'code', 'credits']

    for field in required_fields:
        if field not in data:
            return jsonify({
                'status': 'error',
                'message': f'Missing required field: {field}'
            }), 400

    new_course = {
        'id': course_id_counter,
        'name': data['name'],
        'code': data['code'],
        'credits': data['credits']
    }

    courses_db.append(new_course)
    course_id_counter += 1

    return make_response_json(new_course, 201)


# Look up a course by its ID.
@courses_bp.route('/<int:course_id>', methods=['GET'])
def get_course(course_id):

    course = next((c for c in courses_db if c['id'] == course_id), None)

    if not course:
        return jsonify({
            'status': 'error',
            'message': 'Course not found'
        }), 404

    return make_response_json(course, 200)


# Update only the fields sent in the request.
@courses_bp.route('/<int:course_id>', methods=['PUT'])
def update_course(course_id):

    course = next((c for c in courses_db if c['id'] == course_id), None)

    if not course:
        return jsonify({
            'status': 'error',
            'message': 'Course not found'
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            'status': 'error',
            'message': 'Invalid or missing JSON payload'
        }), 400

    course['name'] = data.get('name', course['name'])
    course['code'] = data.get('code', course['code'])
    course['credits'] = data.get('credits', course['credits'])

    return make_response_json(course, 200)


# Delete a course if it exists.
@courses_bp.route('/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):

    global courses_db

    course = next((c for c in courses_db if c['id'] == course_id), None)

    if not course:
        return jsonify({
            'status': 'error',
            'message': 'Course not found'
        }), 404

    courses_db = [c for c in courses_db if c['id'] != course_id]

    return make_response_json(
        {'message': f'Course {course_id} deleted'},
        200
    )