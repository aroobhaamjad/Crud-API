# Task CRUD API

## What is this?

This is a simple CRUD (create, read, update, delete) REST APT built with FastAPI and Python.

The API manages tasks that are stored in my python list. Each task has:
1. ID: unique identifier
2. Title: description of task
3. Done: Status of task (True or False)

The API suports:
1. Viewing all tasks
2. Viewing a specific task by ID
3. Creating a new task given a description
4. Update "title" or "done" given task ID
5. Delete a task by ID

FastAPI also automatically provides a interactive API documentation through Swagger UI.

## Installation & Running

### 1. Clone the repository
git clone https://github.com/aroobhaamjad/Crud-API.git

cd Crud-API

### 2. Install dependencies
pip install "fastapi[standard]"

### 3. Run the API
python -m fastapi dev main.py

API will be available at: http://localhost:8000

Swagger documentation will be available at: http://localhost:8000/docs

## API Endpoints

| Method | Endpoint    | Description    |
| :---:   | :---: | :---: |
| GET | /   |  Returns basic API information  |
| GET | /health   |  Returns API health status  |
| GET | /tasks   |  Returns all tasks  |
| GET | /tasks/{id}   |  Returns a specific task by ID  |
| POST | /tasks   |  Creates a new task  |
| PUT | /tasks{id}   |  Updates an existing task  |
| DELETE | /tasks{id}   |  Deletes a task  |

## Example Request

### Create a Task

### cURL

curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d '{"title":"Buy milk"}'

### Response

HTTP/1.1 201 Created
content-type: application/json

{
    "title": "Buy milk",
    "id": 3,
    "done": false
}
