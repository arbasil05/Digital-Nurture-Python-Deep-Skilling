# Django REST API

This project uses Django REST Framework (DRF) to build endpoints for managing courses, students, and enrollments.

## How to Run

1. Open your terminal in this directory:
   ```bash
   cd PythonBackFrameworks/Abdur_Rahman_Basil_A_H/handson_03/
   ```
2. Activate the virtual environment:
   * **Windows (PowerShell):**
     ```powershell
     .\.handson03\Scripts\Activate.ps1
     ```
   * **Linux/macOS:**
     ```bash
     source .handson03/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Testing Endpoints

You can check and test these endpoints using your browser or Postman:
* **Courses CRUD:** `http://127.0.0.1:8000/api/courses/`
* **Students CRUD:** `http://127.0.0.1:8000/api/students/`
* **Enrollments CRUD:** `http://127.0.0.1:8000/api/enrollments/`
* **Students in Course:** `http://127.0.0.1:8000/api/courses/<id>/students/` (lists students enrolled in a course)
