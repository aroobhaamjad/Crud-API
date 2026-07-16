from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

memory = [
    {'id': 0, 'title': 'Complete code', 'done': True},
    {'id': 1, 'title': 'test code', 'done': False},
    {'id': 2, 'title': 'Deploy api', 'done': False}
]

app = FastAPI()

@app.get("/")
def read_root():
    """Root endpoint that returns basic information about the API."""
    return {"name": "Task API", "version": "1.0", "endpoint": ["/tasks"]}

@app.get("/health")
def read_health():
    """Health check endpoint that returns the status of the API."""
    return {"status": "ok"}

@app.get("/tasks")
def read_tasks():
    """Endpoint to get all tasks."""
    return memory

@app.get("/tasks/{id}")
def read_task(id: int):
    """Endpoint to get a specific task by its ID."""
    for task in memory:
        if task['id'] == id:
            return task
    raise HTTPException(status_code=404, detail={"error": f"Task {id} not found"})

@app.post("/tasks")
def create_task(task: dict):
    """Endpoint to create a new task."""
    if 'title' not in task:
        raise HTTPException(status_code=400, detail={"error": "Task title is required"})
    
    task['id'] = len(memory)
    task['done'] = False
    memory.append(task)

    return JSONResponse(
        status_code=201,
        content=task
    )