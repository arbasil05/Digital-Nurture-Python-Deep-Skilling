# FastAPI Async Course & Student Manager

This is a FastAPI application that manages courses, students, and course enrollments using async SQLite (SQLAlchemy & aiosqlite). It also demonstrates background tasks by simulating the sending of email confirmations when a student is enrolled.

## How to Run

1. Open your terminal in this directory:
   ```bash
   cd PythonBackFrameworks/Abdur_Rahman_Basil_A_H/handson_07/
   ```
2. Activate the virtual environment:
   * **Windows (PowerShell):**
     ```powershell
     .\.handson07\Scripts\Activate.ps1
     ```
   * **Linux/macOS:**
     ```bash
     source .handson07/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the server:
   ```bash
   uvicorn main:app --reload
   ```
5. The API runs at: `http://127.0.0.1:8000`

## Testing the Endpoints (Interactive API Docs)

Open `http://127.0.0.1:8000/docs` in your browser to view the interactive Swagger interface:
1. **Create a Student**: Call `POST /api/students/` (e.g., `{"name": "Abdur Rahman", "email": "rahman@example.com"}`).
2. **Create a Course**: Call `POST /api/courses/` (e.g., `{"name": "Async Programming", "code": "CS-401", "credits": 4}`).
3. **Enroll Student in Course**: Call `POST /api/enrollments/` with the student ID and course ID.
   * Watch your terminal logs when you enroll: it will run the background task simulating email delivery asynchronously.
4. **Get Course Enrollment List**: Call `GET /api/courses/{course_id}/students/` to see who is enrolled.
