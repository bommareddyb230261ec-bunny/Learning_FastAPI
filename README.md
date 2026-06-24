# FastAPI Products Demo (with Frontend)

A beginner-friendly demo project demonstrating a FastAPI backend connected to a PostgreSQL database and integrated with a tutorial frontend. The project implements a modular backend structure with fully tested CRUD (Create, Read, Update, Delete) operations and simple REST APIs consumed by the frontend.

---

## Project Overview

This repository contains a FastAPI backend that exposes REST APIs for managing a simple product list and a frontend (from a tutorial project) that consumes those APIs. The backend follows a modular structure so components (database, models, and API routes) are easy to understand, extend, and test.

Use cases covered:

- Create new product records
- Read single and multiple product records
- Update existing product records
- Delete product records

## Features

- REST APIs built with FastAPI
- Full CRUD operations for `Product` resources
- PostgreSQL database integration (SQLAlchemy for ORM)
- Frontend integrated and configured to talk to the backend (CORS enabled for localhost:3000)
- Modular backend structure for clarity and maintainability
- Manual testing performed for all CRUD endpoints

## Tech Stack

- Backend: FastAPI
- Database: PostgreSQL (SQLAlchemy for ORM)
- Frontend: React (sourced from a tutorial/project and integrated in `frontend/`)
- Development server: Uvicorn

## Project Structure

- `main.py` — Application entrypoint; mounts routes, middleware, and DB initialization.
- `database.py` — Database session / engine creation (SQLAlchemy setup).
- `database_model.py` — SQLAlchemy declarative models and Base metadata.
- `models.py` — Pydantic models / request/response schemas used by FastAPI endpoints.
- `frontend/` — React frontend (separate package.json, build scripts, and dev server).

This modular layout separates schema, persistence, and API logic so each piece can be tested and evolved independently.

## API Functionality

Base URL: `http://localhost:8000` (default when running with Uvicorn)

Available endpoints:

- `GET /` — Simple status / greeting
- `GET /products` — Returns all products
- `GET /products/{id}` — Returns a single product by id
- `POST /products` — Create a new product
- `PUT /products/{id}` — Update an existing product
- `DELETE /products/{id}` — Delete a product

Request/response format: JSON. The `Product` object expects these fields (example):

```json
{
  "name": "Laptop",
  "description": "Dell Laptop",
  "price": 50000,
  "quantity": 5
}
```

## Database Integration

This project uses PostgreSQL with SQLAlchemy as the ORM. The backend opens a session per request and commits changes for create/update/delete operations.

Environment variable example (used by `database.py` or your configuration):

```
DATABASE_URL=postgresql://<db_user>:<db_password>@localhost:5432/<db_name>
```

Make sure to replace the placeholders with your actual Postgres credentials.

## Setup Instructions

1. Clone the repository and change into the project directory.

2. Create and activate a Python virtual environment (recommended):

```bash
python -m venv myenvironment
# Windows (PowerShell)
myenvironment\Scripts\Activate.ps1
# Windows (cmd)
myenvironment\Scripts\activate.bat
# macOS / Linux
source myenvironment/bin/activate
```

3. Install backend dependencies (example packages used in this project):

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
```

If you have a `requirements.txt`, run:

```bash
pip install -r requirements.txt
```

4. Configure your PostgreSQL database and export the `DATABASE_URL` environment variable.

5. Create the database tables (the app runs `Base.metadata.create_all(bind=engine)` on startup if configured in `main.py`). You can also run any provided DB initialization script if present.

6. Start the backend server (from the project root):

```bash
uvicorn main:app --reload --port 8000
```

7. Start the frontend (opens at http://localhost:3000 by default):

```bash
cd frontend
npm install
npm start
```

The frontend is configured to talk to `http://localhost:8000` by default, and CORS is enabled for `http://localhost:3000` in the backend.

## Quick API Examples

- List products:

```bash
curl http://localhost:8000/products
```

- Create a product:

```bash
curl -X POST http://localhost:8000/products \
  -H "Content-Type: application/json" \
  -d '{"name":"New Item","description":"Example","price":100,"quantity":2}'
```

- Update product id=1:

```bash
curl -X PUT http://localhost:8000/products/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Updated","description":"Updated","price":120,"quantity":3}'
```

- Delete product id=1:

```bash
curl -X DELETE http://localhost:8000/products/1
```

## Future Improvements

- Add automated tests (unit and integration) for API and DB operations
- Add OpenAPI documentation enhancements and example responses
- Add authentication/authorization (JWT or OAuth) for protected endpoints
- Implement database migrations with Alembic
- Add CI pipeline to run tests and linters
- Improve frontend with pagination, search, and input validation UX

---

If you'd like, I can also:

- Add a `requirements.txt` or `pyproject.toml` for reproducible installs
- Add a small `.env.example` and instructions to load env variables
- Create basic unit tests for the CRUD endpoints

Feel free to tell me which of the follow-ups you'd like me to do next.
