# Task Management System

## Requirements
- Python 3.x
- FastAPI
- Uvicorn

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/task-manager.git
    cd task-manager
    ```
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Start the FastAPI application:
    ```bash
    uvicorn app.main:app --reload
    ```

## Testing
- You can test the API using Swagger UI at `http://localhost:8000/docs`.

## Features
- User Registration/Login
- Task Management
- JWT-based Authentication for API
- Session-based Authentication for Web
