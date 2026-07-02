# FastAPI Async Course Manager

This is a FastAPI application that manages courses asynchronously using SQLAlchemy and aiosqlite (async SQLite database connection).

## How to Run

1. Open your terminal in this directory:
   ```bash
   cd PythonBackFrameworks/Abdur_Rahman_Basil_A_H/handson_06/
   ```
2. Create and activate a virtual environment:
   * **Windows (PowerShell):**
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   * **Linux/macOS:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the development server:
   ```bash
   uvicorn main:app --reload
   ```
5. The API is hosted at: `http://127.0.0.1:8000`

## Testing the Endpoints (Interactive API Docs)

FastAPI provides an interactive UI out of the box. Open `http://127.0.0.1:8000/docs` in your browser to view and test all endpoints:
* **POST `/api/courses/`**: Create a new course.
* **GET `/api/courses/`**: List all courses (supports filtering by `department_id` and query pagination parameters `skip` and `limit`).
* **GET `/api/courses/{course_id}`**: Get a specific course.
* **PUT `/api/courses/{course_id}`**: Update a course's fields.
* **DELETE `/api/courses/{course_id}`**: Remove a course.
