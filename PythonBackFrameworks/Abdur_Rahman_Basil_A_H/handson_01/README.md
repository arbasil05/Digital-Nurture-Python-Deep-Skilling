# Django Basic Setup

This is a simple Django project that sets up a basic course manager server.

## How to Run

1. Open your terminal in this directory:
   ```bash
   cd PythonBackFrameworks/Abdur_Rahman_Basil_A_H/handson_01/
   ```
2. Activate the virtual environment:
   * **Windows (PowerShell):**
     ```powershell
     .\.handson01\Scripts\Activate.ps1
     ```
   * **Linux/macOS:**
     ```bash
     source .handson01/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations (to set up the local SQLite database):
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Open your browser and visit:
   `http://127.0.0.1:8000/api/hello/` to see the running message.
