# FastAPI Auth System

This is a FastAPI-based backend that handles user registration, login (using OAuth2 with JWT tokens), and basic course management. It uses an SQLite database with SQLAlchemy (async).

## How to Run

1. Open your terminal in this directory:
   ```bash
   cd PythonBackFrameworks/Abdur_Rahman_Basil_A_H/handson_09/
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
   uvicorn main:app --reload
   ```
5. The server will run at: `http://127.0.0.1:8000`

## Testing the Endpoints (Interactive API Docs)

FastAPI has automatic documentation. Open `http://127.0.0.1:8000/docs` in your browser to test endpoints:

1. **Register a User:**
   * Click **POST `/api/auth/register/`** -> "Try it out".
   * Send a JSON body like:
     ```json
     {
       "email": "test@example.com",
       "password": "mysecurepassword"
     }
     ```
2. **Login & Get Token:**
   * Click the green **Authorize** button on the top right, OR click **POST `/api/auth/login/`** -> "Try it out".
   * Enter the registered email and password to log in. This returns a Bearer JWT token.
3. **Access Protected Endpoints:**
   * Once authorized/logged in, you can create a new course using **POST `/api/courses/`**.
   * Retrieve your profile info using **GET `/api/users/me/`**.
