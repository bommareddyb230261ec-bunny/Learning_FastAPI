# FastAPI Products Demo

A beginner-friendly backend project built using FastAPI and PostgreSQL.
This project demonstrates CRUD operations, database integration, and frontend-backend connectivity.

---

## Project Overview

This project is a simple Products Management API developed using FastAPI.

The backend was fully implemented and connected with a PostgreSQL database using SQLAlchemy ORM. A tutorial-based frontend was integrated with the backend APIs to test all CRUD functionalities successfully.

The project follows a modular backend structure for better readability and maintainability.

---

## Features

- REST API development using FastAPI
- PostgreSQL database integration
- SQLAlchemy ORM support
- Full CRUD operations
- Frontend and backend integration
- JSON-based API communication
- Modular backend structure
- API testing using frontend and Swagger UI

---

## Tech Stack

- Backend: FastAPI
- Database: PostgreSQL
- ORM: SQLAlchemy
- Frontend: React (tutorial-based frontend)
- Server: Uvicorn
- Language: Python

---

## CRUD Operations

The application supports:

- Create Products
- Read Products
- Update Products
- Delete Products

---

## API Endpoints

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| GET    | `/products`      | Get all products  |
| GET    | `/products/{id}` | Get product by ID |
| POST   | `/products`      | Create a product  |
| PUT    | `/products/{id}` | Update a product  |
| DELETE | `/products/{id}` | Delete a product  |

---

## Example Product JSON

```json
{
  "name": "Laptop",
  "description": "Dell Laptop",
  "price": 50000,
  "quantity": 5
}
```

---

## Project Structure

```bash
project/
│── main.py
│── database.py
│── database_model.py
│── models.py
│── frontend/
│── requirements.txt
│── README.md
```

### File Description

- `main.py` → FastAPI application entry point
- `database.py` → Database connection setup
- `database_model.py` → SQLAlchemy database models
- `models.py` → Pydantic schemas
- `frontend/` → Connected frontend application

---

## Database Integration

This project uses PostgreSQL with SQLAlchemy ORM for database operations.

Example database configuration:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repository-url>
cd <project-folder>
```

## 2. Create Virtual Environment

```bash
python -m venv myenvironment
```

Activate environment:

### Windows

```bash
myenvironment\Scripts\activate
```

### Linux / macOS

```bash
source myenvironment/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run FastAPI Server

```bash
uvicorn main:app --reload
```

Backend runs at:

```bash
http://localhost:8000
```

Swagger API documentation:

```bash
http://localhost:8000/docs
```

---

## 5. Run Frontend

```bash
cd frontend
npm install
npm start
```

---

## My Contribution

In this project, I worked mainly on backend development using FastAPI.

My contributions include:

- Building REST APIs
- Implementing CRUD operations
- Connecting PostgreSQL database
- Integrating frontend with backend
- Testing API endpoints
- Organizing backend files in modular format

The frontend was adapted from a tutorial project and connected with the backend APIs.

---

## Learning Outcome

Through this project, I learned:

- FastAPI fundamentals
- REST API development
- PostgreSQL integration
- SQLAlchemy ORM
- Frontend-backend communication
- CRUD application workflow
- API testing and debugging
