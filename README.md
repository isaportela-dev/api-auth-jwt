# 🔐 JWT Authentication API (FastAPI)

<!-- API de autenticação profissional com FastAPI, PostgreSQL e Docker -->

A production-ready authentication API built with **FastAPI**, implementing user registration, login, and route protection using **JWT (JSON Web Tokens)** and **OAuth2**. Designed with a layered architecture, containerized with Docker, and backed by a real PostgreSQL database.

---

## 🚀 Features

- User registration with secure password hashing (PBKDF2)
- Login with JWT token generation
- OAuth2 authentication flow
- Protected route (`/profile`) with token validation
- Layered architecture (routers, services, schemas, models)
- PostgreSQL database with SQLAlchemy ORM
- Containerized with Docker and docker-compose
- Auto-generated API documentation with Swagger UI

---

## 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main language |
| FastAPI | Web framework |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM |
| Alembic | Database migrations |
| Docker & docker-compose | Containerization |
| Python-Jose | JWT encoding/decoding |
| Passlib (PBKDF2) | Password hashing |
| Uvicorn | ASGI server |

---

## 📁 Project Structure

<!-- Arquitetura em camadas — cada arquivo tem uma única responsabilidade -->
```
api-auth-jwt/
├── app/
│   ├── main.py              # App entry point
│   ├── core/
│   │   ├── database.py      # Database connection and session
│   │   └── security.py      # JWT and password hashing
│   ├── models/
│   │   └── user.py          # SQLAlchemy User model
│   ├── schemas/
│   │   └── user.py          # Pydantic schemas
│   ├── routers/
│   │   └── auth.py          # Route definitions
│   └── services/
│       └── auth.py          # Business logic
├── migrations/              # Alembic migrations
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## ▶️ Running the project

<!-- A forma mais fácil de rodar — um único comando sobe tudo -->

Make sure you have [Docker](https://www.docker.com/) installed, then run:
```bash
docker-compose up --build
```

This will start both the API and the PostgreSQL database automatically.

Access the API documentation at:
```
http://127.0.0.1:8000/docs
```

---

## 🔑 Authentication Flow

<!-- Fluxo completo de autenticação -->

### 1. Register a user
**POST /register**
```json
{
  "username": "isabella",
  "password": "yourpassword"
}
```

### 2. Login
**POST /login**

Returns a JWT access token.

### 3. Authorize
Click **Authorize 🔒** in Swagger UI and enter your credentials.

### 4. Access protected route
**GET /profile**

Returns the authenticated user's data.

---

## 👩‍💻 Author

**Isabella Portela**
Veterinary Medicine graduate | Systems Analysis and Development student
Full Stack Developer (Backend focused) in training (Python & Java)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Isabella%20Portela-blue?style=flat&logo=linkedin)](https://linkedin.com/in/isabellarportela)
[![GitHub](https://img.shields.io/badge/GitHub-isaportela--dev-black?style=flat&logo=github)](https://github.com/isaportela-dev)