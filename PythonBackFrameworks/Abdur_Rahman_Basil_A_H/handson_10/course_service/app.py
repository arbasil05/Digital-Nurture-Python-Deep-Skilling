import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('courses.db')
    conn.execute('CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
    conn.commit()
    conn.close()

@app.route("/api/courses", methods=["GET", "POST"])
def manage_courses():
    conn = sqlite3.connect('courses.db')
    try:
        cursor = conn.cursor()
        if request.method == 'POST':
            data = request.get_json()
            cursor.execute("INSERT INTO courses (name) VALUES (?)", (data['name'],))
            conn.commit()
            return jsonify({"message": "Course created successfully!"}), 201
        
        cursor.execute("SELECT id, name FROM courses")
        courses = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]
        return jsonify(courses), 200
    finally:
        conn.close()

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    conn = sqlite3.connect('courses.db')
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM courses WHERE id = ?", (course_id,))
        row = cursor.fetchone()
        
        if row:
            return jsonify({"id": row[0], "name": row[1]}), 200
        return jsonify({"error": "Course not found"}), 404
    finally:
        conn.close()

if __name__ == "__main__":
    init_db()
    app.run(port=5001,debug=True)