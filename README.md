# 🔐 JWT Authentication API (FastAPI)

<!-- API de autenticação profissional com FastAPI, PostgreSQL e Docker -->

A production-ready authentication API built with **FastAPI**, implementing user registration, login, and route protection using **JWT (JSON Web Tokens)** and **OAuth2**. Designed with a layered architecture, containerized with Docker, and backed by a real PostgreSQL database.

---

## 🚀 Features

- User registration with secure password hashing (PBKDF2)
- Password strength validation (minimum 8 chars, uppercase, number and special character)
- Login with JWT access token + refresh token generation
- Token refresh endpoint — renew access without re-login
- OAuth2 authentication flow
- Protected route (`/profile`) with token validation
- Rate limiting: 5 requests/min on `/login`, 3 requests/min on `/register`
- Layered architecture (routers, services, schemas, models)
- PostgreSQL database with SQLAlchemy ORM
- Containerized with Docker and docker-compose
- Auto-generated API documentation with Swagger UI
- Token blacklist — logout invalidates the token immediately
- Security headers middleware (X-Frame-Options, X-Content-Type-Options, HSTS, CSP)
- Automated tests with pytest — 10 tests covering auth flow, security and edge cases

---

## 🔒 Security Practices (OWASP Top 10)

| OWASP | Vulnerability | Mitigation |
|---|---|---|
| A01 | Broken Access Control | Protected routes with JWT token validation |
| A02 | Cryptographic Failures | Passwords hashed with PBKDF2 — never stored in plain text |
| A03 | Injection | SQLAlchemy ORM with parameterized queries — no raw SQL |
| A07 | Identification & Authentication Failures | Password strength validation, JWT expiration, refresh token, rate limiting |
| A05 | Security Misconfiguration | Sensitive data stored in environment variables via python-dotenv |
| A01 | Broken Access Control | Protected routes with JWT + token blacklist on logout |
| A08 | Security Misconfiguration | Security headers via middleware (HSTS, CSP, X-Frame-Options) |

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

### 5. Logout
**POST /logout**
Invalidates the current token — added to blacklist immediately.

### 6. Refresh token
**POST /refresh**
Renews the access token using a valid refresh token.

---

## 👩‍💻 Author

**Isabella Portela**
Desenvolvedora Full Stack | Python · FastAPI · Java · Spring Boot
[LinkedIn](https://linkedin.com/in/isabellarportela) · [GitHub](https://github.com/isaportela-dev)