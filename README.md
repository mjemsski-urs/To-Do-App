# 📝 To-Do List Web App using Flask + REST API

This is a full-featured **To-Do List Web Application** built with **Python**, **Flask**, **SQLite**, and **Bootstrap**, enhanced with a **RESTful API**. It supports both a traditional web interface and API endpoints for managing users and tasks. Users can register, log in, and manage tasks from the browser or via HTTP requests.

---

## 🚀 Features

- ✅ User Registration and Login
- ✅ Add, Edit, and Delete Tasks
- 🔄 Toggle Task Completion Status
- 🔐 Session Management with Flask
- 🌐 REST API with JSON Support
- 📊 Swagger UI for API Documentation
- 🧪 Automated Testing with Pytest + Coverage
- 🎨 Responsive UI with Bootstrap
- 🧠 SQLite Database with SQLAlchemy ORM

---

## 📦 Tech Stack

| Technology     | Description                       |
|----------------|-----------------------------------|
| Python         | Backend Programming Language       |
| Flask          | Lightweight Web Framework          |
| SQLAlchemy     | ORM for Database Interaction       |
| SQLite         | Embedded Local Database            |
| HTML/CSS       | Frontend Structure & Styling       |
| Bootstrap      | Responsive Design Framework        |
| JavaScript     | UI Behavior Enhancements           |
| Flasgger       | Swagger UI for API Docs            |
| Pytest         | Testing Framework                  |

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/todo-app.git
cd todo-app
```

### 2. (Optional) Create a virtual environment
```bash
python -m venv venv
venv/bin/activate
```

### 4. Run the application
```bash
python app.py
```

### 5. Visit the app
Open your browser and go to:
👉 http://localhost:5000

---

## Run Tests

- Unit tests for the API are included in tests/test_api.py. Use pytest to run them and measure test coverage:

```bash
pytest tests --cov=api --cov-report=term-missing
```

This command will:

- Run all test cases
- Show coverage percentage
- Highlight which lines of code are untested

---
