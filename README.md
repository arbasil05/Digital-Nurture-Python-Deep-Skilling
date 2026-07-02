# Deep Skilling Solutions Repository

Welcome to the **Deep Skilling Solutions** learning repository. This repository organizes various hands-on projects and exercises covering both Frontend Development and Python Backend Frameworks.

---

## 📂 Repository Structure

The codebase is organized into three primary segments:
1. **Frontend Development (`Module2_FrontendDev`)**: Focused on user interface design, styling, and client-side scripting.
2. **Database Integration (`Module3_DatabaseIntegration`)**: Focused on database schema design, normalization, referential integrity, and SQL DDL operations.
3. **Python Backend Frameworks (`PythonBackFrameworks`)**: Focused on server-side applications, database ORMs, REST APIs, and microservices.

---

## 🎨 Module 1: Frontend Development

Access the main frontend directory: **[Frontend Workspace](./Module2_FrontendDev/Abdur_Rahman_Basil_A_H/)**

| Hands-on Module | Description | Quick Link |
| :--- | :--- | :--- |
| 🔹 **Hands-on 01** | HTML & CSS layout structure, grid/flexbox, typography, and styling foundation. | **[Open Folder 📂](./Module2_FrontendDev/Abdur_Rahman_Basil_A_H/handson_01/)** |
| 🔹 **Hands-on 02** | JavaScript dynamic DOM manipulation, event handling, AJAX/fetch integration. | **[Open Folder 📂](./Module2_FrontendDev/Abdur_Rahman_Basil_A_H/handson_02/)** |

---

## ⚙️ Module 2: Python Backend Frameworks

Access the main backend directory: **[Backend Workspace](./PythonBackFrameworks/Abdur_Rahman_Basil_A_H/)**

| Hands-on Module | Framework | Description | Quick Link |
| :--- | :--- | :--- | :--- |
| 🔸 **Hands-on 01** | **Django** | Request-response lifecycle, basic routing, and views. | **[Open Folder 📂](./PythonBackFrameworks/Abdur_Rahman_Basil_A_H/handson_01/)** |
| 🔸 **Hands-on 02** | **Django** | Database migrations, ORM models, and relationship queries. | **[Open Folder 📂](./PythonBackFrameworks/Abdur_Rahman_Basil_A_H/handson_02/)** |
| 🔸 **Hands-on 03** | **Django REST** | Model serializers, API views, and RESTful CRUD endpoints. | **[Open Folder 📂](./PythonBackFrameworks/Abdur_Rahman_Basil_A_H/handson_03/)** |
| 🔸 **Hands-on 04** | **Flask** | Server setup, blueprints, routes, custom error handlers. | **[Open Folder 📂](./PythonBackFrameworks/Abdur_Rahman_Basil_A_H/handson_04/)** |
| 🔸 **Hands-on 05** | **Flask** | SQLAlchemy database integration, migrations, and CRUD operations. | **[Open Folder 📂](./PythonBackFrameworks/Abdur_Rahman_Basil_A_H/handson_05/)** |
| 🔸 **Hands-on 06** | **FastAPI** | Lifespan events, Pydantic validations, aiosqlite integration. | **[Open Folder 📂](./PythonBackFrameworks/Abdur_Rahman_Basil_A_H/handson_06/)** |
| 🔸 **Hands-on 07** | **FastAPI** | Asynchronous repository pattern, dependency injection, SQLite operations. | **[Open Folder 📂](./PythonBackFrameworks/Abdur_Rahman_Basil_A_H/handson_07/)** |
| 🔸 **Hands-on 09** | **FastAPI** | User authentication (OAuth2 & JWT), password hashing, and async SQLAlchemy/SQLite database integration. | **[Open Folder 📂](./PythonBackFrameworks/Abdur_Rahman_Basil_A_H/handson_09/)** |
| 🔸 **Hands-on 10** | **Flask** | Microservices architecture (Course Service, Student Service, Gateway proxy) with HTTP/REST inter-service communication. | **[Open Folder 📂](./PythonBackFrameworks/Abdur_Rahman_Basil_A_H/handson_10/)** |

---

## 🗄️ Module 3: Database Integration

Access the main database integration directory: **[Database Integration Workspace](./Module3_DatabaseIntegration/Abdur_Rahman_Basil_AH/)**

| Hands-on Module | Description | Quick Link |
| :--- | :--- | :--- |
| 🔹 **Hands-on 01** | Database schema design, SQL DDL (CREATE/ALTER/DROP), constraints, normalisation, and referential integrity. | **[Open Folder 📂](./Module3_DatabaseIntegration/Abdur_Rahman_Basil_AH/handson_01/)** |

---

## 🛠️ Setup Instructions

Each backend folder contains a `requirements.txt` file. To run any backend module:

1. Navigate to the desired module folder:
   ```bash
   cd PythonBackFrameworks/Abdur_Rahman_Basil_A_H/handson_XX/
   ```
2. Create and activate a virtual environment:
   - On Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - On Linux/macOS:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the development server (Django, Flask, or FastAPI uvicorn command).
