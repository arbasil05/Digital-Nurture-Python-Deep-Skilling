from flask import Flask, request, jsonify
import sqlite3
import requests

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect('students.db')
    conn.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)')
    conn.commit()
    conn.close()

@app.route('/api/students', methods=['GET', 'POST'])
def manage_students():
    conn = sqlite3.connect('students.db')
    try:
        cursor = conn.cursor()
        
        if request.method == 'POST':
            data = request.get_json()
            cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", (data['name'], data['email']))
            conn.commit()
            return jsonify({"message": "Student created successfully!"}), 201
            

        cursor.execute("SELECT id, name, email FROM students")
        students = [{"id": row[0], "name": row[1], "email": row[2]} for row in cursor.fetchall()]
        return jsonify(students), 200
    finally:
        conn.close()

@app.route('/api/students/<int:student_id>/enroll', methods=['POST'])
def enroll_student(student_id):
    data = request.get_json()
    course_id = data.get('course_id')
    

    try:
        response = requests.get(f'http://127.0.0.1:5001/api/courses/{course_id}')
        
        if response.status_code == 404:
            return jsonify({"error": "Cannot enroll: Course does not exist"}), 404
            
     
        conn = sqlite3.connect('students.db')
        try:
            cursor = conn.cursor()
         
            cursor.execute('''CREATE TABLE IF NOT EXISTS enrollments 
                              (student_id INTEGER, course_id INTEGER, 
                              UNIQUE(student_id, course_id))''')
            
            cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)", 
                           (student_id, course_id))
            conn.commit()
            
            return jsonify({
                "message": f"Success! Student {student_id} enrolled in Course {course_id}",
                "course_details": response.json()
            }), 201
            
        except sqlite3.IntegrityError:
            return jsonify({"error": "Student is already enrolled in this course!"}), 409
        finally:
            conn.close()

    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Course Service is currently unavailable. Please try again later."}), 503
        
if __name__ == '__main__':
    init_db()
    app.run(port=5002, debug=True)