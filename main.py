from fastapi import FastAPI, HTTPException

memory = [
    {'id': 0, 'title': 'Complete code', 'done': True},
    {'id': 1, 'title': 'test code', 'done': False},
    {'id': 2, 'title': 'Deploy api', 'done': False}
]

app = FastAPI()

@app.get("/")
def read_root():
    return {"name": "Task API", "version": "1.0", "endpoint": ["/tasks"]}

@app.get("/health")
def read_health():
    return {"status": "ok"}

@app.get("/tasks")
def read_tasks():
    return memory

@app.get("/tasks/{id}")
def read_task(id: int):
    for task in memory:
        if task['id'] == id:
            return task
    raise HTTPException(status_code=404, detail={"error": f"Task {id} not found"})