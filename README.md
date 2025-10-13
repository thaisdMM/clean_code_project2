# Clean Code Project

A Python web application built with Flask following clean architecture principles. This project demonstrates a well-structured codebase with separation of concerns, dependency inversion, and testable components.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Technologies Used](#technologies-used)

## Features

- User creation and retrieval
- RESTful API design
- Error handling with custom HTTP exceptions
- Database operations with SQLAlchemy
- Clean architecture implementation
- Unit tests for controllers and repositories

## Architecture

This project follows the Clean Architecture pattern, which emphasizes separation of concerns and dependency inversion. The architecture consists of:

1. **Controllers**: Handle business logic
2. **Models**: Manage data and database interactions
3. **Views**: Format HTTP requests and responses
4. **Validators**: Validate input data and handle errors
5. **Main**: Composition root that wires everything together

The dependency flow is from outer layers to inner layers, with the core business logic at the center.

## Project Structure

```
.
├── init/
│   └── schema.sql          # Database schema
├── src/
│   ├── controllers/        # Business logic
│   │   ├── interfaces/     # Controller interfaces
│   │   ├── user_creator.py # Create user logic
│   │   └── user_finder.py  # Find user logic
│   ├── main/               # Application entry point and composition
│   │   ├── composer/       # Dependency injection
│   │   ├── routes/         # API routes
│   │   └── server/         # Flask application setup
│   ├── models/             # Data layer
│   │   ├── connection/     # Database connection handling
│   │   ├── entities/       # Data models
│   │   └── repositories/   # Data access layer
│   ├── validators/         # Input validation and error handling
│   │   ├── error_types/    # Custom HTTP exceptions
│   │   └── errors/         # Error handlers
│   └── views/              # HTTP request/response formatting
│       ├── http_types/     # HTTP request/response classes
│       ├── user_creator_view.py
│       └── user_finder_view.py
├── requirements.txt        # Python dependencies
└── run.py                 # Application entry point
```

## Prerequisites

- Python 3.8+
- pip (Python package installer)
- SQLite (comes pre-installed with Python)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd clean_code_project
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

The application uses SQLite as its database. To initialize the database:

1. Create a database file:

   ```bash
   touch database.db
   ```

2. Apply the schema:
   ```bash
   sqlite3 database.db < init/schema.sql
   ```

## Running the Application

To start the Flask development server:

```bash
python run.py
```

The application will be available at `http://localhost:3000`.

## API Endpoints

### Create User

```http
POST /user
```

**Request Body:**

```json
{
  "person_name": "John Doe",
  "age": 30,
  "height": 5.9
}
```

**Response:**

```json
{
  "Type": "Users",
  "count": 1,
  "message": "Usuario cadastrado com sucesso!"
}
```

### Find User

```http
GET /user/find/{person_name}
```

**Response:**

```json
{
  "Type": "Users",
  "count": 1,
  "atributes": [
    {
      "id": 1,
      "person_name": "John Doe",
      "age": 30
    }
  ]
}
```

## Testing

Run the unit tests with pytest:

```bash
pytest
```

Or run tests for specific modules:

```bash
pytest src/controllers/user_creator_test.py
pytest src/models/repositories/users_repository_test.py
```

## Technologies Used

- [Python](https://www.python.org/) - Programming language
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM for database operations
- [Pytest](https://docs.pytest.org/) - Testing framework
- [SQLite](https://www.sqlite.org/) - Database engine
