# 🚀 Django Portfolio REST API

<div align="center">

![Django](https://img.shields.io/badge/Django-5.2-green?style=for-the-badge\&logo=django)
![Django REST Framework](https://img.shields.io/badge/DRF-REST%20API-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge\&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge\&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

### Backend API for My Dynamic Portfolio Website

A production-ready Django REST API powering a modern Next.js portfolio with dynamic content management through the Django Admin Panel.

</div>

---

# 📖 Overview

This project is the backend service for my personal portfolio website. It exposes RESTful APIs built with **Django** and **Django REST Framework**, allowing the frontend application to dynamically retrieve portfolio content.

Instead of hardcoding information into the frontend, every section—including profile details, projects, skills, testimonials, and contact information—is managed through the Django Admin dashboard.

---

# 🌐 Live Architecture

```text
                Next.js Frontend
                     │
                     ▼
           Django REST API (This Repo)
                     │
                     ▼
          SQLite Database + Media Files
```

---

# ✨ Features

## 👤 Profile API

* Dynamic Profile Information
* Hero Section Content
* About Section Content
* Resume Download
* Profile Image
* Contact Details

---

## 💼 Projects API

* Dynamic Project Listing
* Project Images
* Feature Highlights
* GitHub Links
* Live Demo Links
* Display Ordering
* Active/Inactive Projects

---

## ⚡ Skills API

* Technical Skills
* Skill Categories
* Skill Icons
* Progress Values
* Display Ordering

---

## 💬 Testimonials API

* Client Reviews
* Client Images
* Client Position
* Company Information
* Dynamic Testimonials

---

## 📩 Contact API

* Email Information
* Phone Number
* Location
* Social Links

---

## ⚙ Admin Dashboard

Everything can be managed without changing the frontend code.

The admin panel allows you to:

* Manage Profile
* Manage Skills
* Manage Projects
* Manage Testimonials
* Upload Images
* Upload Resume
* Control Display Order
* Enable / Disable Content

---

# 🛠 Technologies Used

### Backend

* Python 3.12
* Django
* Django REST Framework

### Database

* SQLite

### Media

* Pillow

### API

* RESTful JSON APIs

### Deployment

* PythonAnywhere (Recommended)

---

# 📚 API Endpoints

| Endpoint             | Description       |
| -------------------- | ----------------- |
| `/api/profile/`      | Portfolio Profile |
| `/api/projects/`     | Projects          |
| `/api/skills/`       | Skills            |
| `/api/testimonials/` | Testimonials      |
| `/admin/`            | Django Admin      |

---

# 📂 Project Structure

```text
MyDjangoProject/
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── portfolio/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/MuhammadHaseeb3112/myportfolio-django-api.git
```

Move into the project

```bash
cd myportfolio-django-api
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Apply migrations

```bash
python manage.py migrate
```

Create an admin user

```bash
python manage.py createsuperuser
```

Run the development server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

# ⚙ Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key

DEBUG=True

ALLOWED_HOSTS=127.0.0.1,localhost

GOOGLE_CLIENT_ID=your_google_client_id

GOOGLE_CLIENT_SECRET=your_google_client_secret
```

---

# 🔐 Security

* Environment Variables
* Secret Key Protection
* Google OAuth Credentials
* Django ORM
* CSRF Protection
* XSS Protection
* Secure Media Handling

---

# 📈 Future Improvements

* JWT Authentication
* PostgreSQL Support
* Docker
* Swagger Documentation
* Rate Limiting
* Redis Cache
* Email Notifications
* CI/CD Pipeline
* Unit Testing

---

# 🔗 Frontend Repository

The frontend application built with **Next.js**, **TypeScript**, and **Tailwind CSS** is available here:

👉 **https://github.com/MuhammadHaseeb3112/myportfolio-nextjs**

---

# 👨‍💻 Author

**Muhammad Haseeb**

Python & Django Developer

GitHub:
https://github.com/MuhammadHaseeb3112

---

# ⭐ Support

If you found this project helpful, please consider giving it a **Star ⭐** on GitHub. It helps others discover the project and supports my work.
