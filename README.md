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

