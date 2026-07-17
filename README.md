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

# AI vs me

## My prompt

Write apis in python using fastapi. you should have a list of tasks in a variable which has title, id and done (true/false)

There should be 5 endpoints: get all tasks, get task by id, create task using title and done should be set to false by default, update task by title or done, and delete task by id

For get all tasks, return 200 status code

For get task by id return 200 status code if id found else send 404

For create task return 201 if created succesfully else return 400 if title not given in body or body is empty

For update task return 200 if sucessful else return 400 if body is empty or title/done missing values or 404 if id not found

For delete return return 204 if deleted else 404 if id not found

Apis should work in browser utilizing swagger ui and also in terminal using curl

## Differences between AI and Me?

1. Used Pydantic by creating BaseModel classes for TaskCreate and TaskUpdate and using status_code parameter in @app.get

2. In delete AI has used tasks.pop(index) whereas I used tasks.remove(task) to avoid adding an unnecassary index variable to memory

3. AI version did not add any docstrings to the functions
