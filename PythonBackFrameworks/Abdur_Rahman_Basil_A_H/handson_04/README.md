# Flask In-Memory API

This is a Flask-based API for course management. It uses Blueprints to structure routing and runs with an in-memory list as a database.

## How to Run

1. Open your terminal in this directory:
   ```bash
   cd PythonBackFrameworks/Abdur_Rahman_Basil_A_H/handson_04/
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
4. Start the server:
   ```bash
   python flask_coursemanage/app.py
   ```
5. The app runs at: `http://127.0.0.1:5000/`

## Testing the Endpoints

Use an API client (like Postman or curl) to test these endpoints:
* **Create Course:** `POST` to `http://127.0.0.1:5000/api/courses/` with JSON:
  ```json
  {
    "name": "Flask Intro",
    "code": "FLASK-01",
    "credits": 3
  }
  ```
* **List Courses:** `GET` to `http://127.0.0.1:5000/api/courses/`
* **Get Course:** `GET` to `http://127.0.0.1:5000/api/courses/<id>`
* **Update Course:** `PUT` to `http://127.0.0.1:5000/api/courses/<id>` with fields you want to update.
* **Delete Course:** `DELETE` to `http://127.0.0.1:5000/api/courses/<id>`
