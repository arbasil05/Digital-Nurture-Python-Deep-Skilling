# Flask API with SQLAlchemy

This is a Flask-based Course Management API that uses SQLAlchemy (SQLite database) and Flask-Migrate for database schema tracking.

## How to Run

1. Open your terminal in this directory:
   ```bash
   cd PythonBackFrameworks/Abdur_Rahman_Basil_A_H/handson_05/
   ```
2. Activate the virtual environment:
   * **Windows (PowerShell):**
     ```powershell
     .\.handson05\Scripts\Activate.ps1
     ```
   * **Linux/macOS:**
     ```bash
     source .handson05/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations to set up the database tables:
   ```bash
   cd flask_coursemanage
   flask db upgrade
   cd ..
   ```
5. Start the Flask application:
   ```bash
   python flask_coursemanage/app.py
   ```
6. The app runs at: `http://127.0.0.1:5000/`

## Testing the Endpoints

Use Postman or curl to test these endpoints:
* **Create Course:** `POST` to `http://127.0.0.1:5000/api/courses/` with JSON:
  ```json
  {
    "name": "Database Systems",
    "code": "CS-302",
    "credits": 4,
    "department_id": 1
  }
  ```
* **List Courses:** `GET` to `http://127.0.0.1:5000/api/courses/`
* **Get Single Course:** `GET` to `http://127.0.0.1:5000/api/courses/<id>`
* **Update Course:** `PUT` to `http://127.0.0.1:5000/api/courses/<id>`
* **Delete Course:** `DELETE` to `http://127.0.0.1:5000/api/courses/<id>`
* **Get Enrolled Students:** `GET` to `http://127.0.0.1:5000/api/courses/<id>/students/`
