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
    """Endpoint to get basic information about the API."""
    return {"name": "Task API", "version": "1.0", "endpoint": ["/tasks"]}

@app.get("/health")
def read_health():
    """Endpoint to get the status of the API."""
    return {"status": "ok"}

@app.get("/tasks")
def read_tasks(search: str = ""):
    """Endpoint to get all or search tasks."""
    if search == "":
        return memory
    
    result = []
    for task in memory:
        if search.lower() in task['title'].lower():
            result.append(task)         

    return result

@app.get("/tasks/{id}")
def read_task(id: int):
    """Endpoint to get a specific task by its id."""
    for task in memory:
        if task['id'] == id:
            return task
    raise HTTPException(status_code=404, detail={"error": f"Task {id} not found"})

@app.post("/tasks")
def create_task(task: dict):
    """Endpoint to create a new task."""
    if 'title' not in task or task['title'] == "":
        raise HTTPException(status_code=400, detail={"error": "Task title is required"})
    
    task['id'] = len(memory)
    task['done'] = False
    memory.append(task)

    return JSONResponse(
        status_code=201,
        content=task
    )

@app.put("/tasks/{id}")
def update_task(id: int, updated_task: dict):
    """Endpoint to update an existing task by its id."""
    if 'title' not in updated_task and 'done' not in updated_task and 'title' == ""  and 'done' == "":
        raise HTTPException(status_code=400, detail={"error": "Title or done must be given"})
    
    for task in memory:
        if task['id'] == id:
            task.update(updated_task)
            return task
    raise HTTPException(status_code=404, detail={"error": f"Task {id} not found"})
    
@app.delete("/tasks/{id}")
def delete_task(id: int):
    """Endpoint to delete a task by its id."""
    for task in memory:
        if task['id'] == id:
            memory.remove(task)
            return JSONResponse(
                status_code=204,
                content={})
    raise HTTPException(status_code=404, detail={"error": f"Task {id} not found"})

@app.get("/stats")
def get_stats():
    """Endpoint to get statistics about the tasks."""
    total = len(memory)
    done = 0
    for task in memory:
        if task['done']:
            done += 1
    open_tasks = total - done

    return {"total": total, "done": done, "open": open_tasks}