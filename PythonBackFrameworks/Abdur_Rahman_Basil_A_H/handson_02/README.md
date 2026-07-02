# Django Models and Database Queries

This project defines Django models for Courses, Students, Departments, and Enrollments, showing how to query relationships using Django's ORM.

## How to Run

1. Open your terminal in this directory:
   ```bash
   cd PythonBackFrameworks/Abdur_Rahman_Basil_A_H/handson_02/
   ```
2. Activate the virtual environment:
   * **Windows (PowerShell):**
     ```powershell
     .\.handson02\Scripts\Activate.ps1
     ```
   * **Linux/macOS:**
     ```bash
     source .handson02/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run database migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Open your browser and visit:
   `http://127.0.0.1:8000/api/hello/` to see the running message.
