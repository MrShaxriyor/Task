# 🧩 Task Manager API (Django REST Framework + JWT)

## 📌 Project Overview

Task Manager REST API built with **Django REST Framework** that provides secure user authentication using **JWT tokens** and allows authenticated users to manage their personal tasks.

Each user can **only access their own tasks**, ensuring proper object-level security.

---

## 🚀 Features

* User Registration (username, email, password confirmation)
* Email-based Login
* JWT Authentication (Access & Refresh Tokens)
* Token Refresh Endpoint
* Protected Task CRUD API
* PostgreSQL Database Integration
* Global Exception Handling
* Deadline support for tasks
* Object Level Permission (User Task Isolation)

---

## 🛠 Tech Stack

* Python
* Django
* Django REST Framework
* SimpleJWT
* PostgreSQL

---

## 🔐 Authentication

### Register

`POST /api/register/`

### Login

`POST /api/login/`

Returns:

* Access Token
* Refresh Token

### Refresh Token

`POST /api/token/refresh/`

### Authorization Header

```
Authorization: Bearer ACCESS_TOKEN
```

---

## 📡 Task Endpoints

* `GET /api/tasks/` → List all user tasks
* `POST /api/tasks/` → Create task
* `GET /api/tasks/{id}/` → Retrieve task
* `PUT /api/tasks/{id}/` → Update task
* `PATCH /api/tasks/{id}/` → Partial update
* `DELETE /api/tasks/{id}/` → Delete task

---

## 🗄 Task Fields

* title
* description
* is_completed
* deadline
* created_at

---

## ⚠️ Error Response Format

All API errors return structured JSON:

```json
{
  "success": false,
  "errors": {},
  "status_code": 400
}
```

---

## 🔒 Security Highlights

* JWT Authentication
* Password Hashing (Django default PBKDF2)
* Authenticated Permissions
* User-based Task Filtering
* Token Expiration & Refresh Flow

---

## 📮 Postman API Documentation

Full API documentation and request examples:

👉 **Postman Docs:**
https://documenter.getpostman.com/view/47089154/2sBXigNECC

---

## ▶️ Run Project Locally

```bash
git clone github.com/MrShaxriyor/Task.git
cd task
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 👨‍💻 Author

Backend Developer Test Project
Built with Django REST Framework
