from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Task API")


tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Build API",
        "done": True
    }
]


# Models
class TaskCreate(BaseModel):
    title: Optional[str] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None



# 1. Get all tasks
@app.get("/tasks", status_code=200)
def get_all_tasks():
    return tasks



# 2. Get task by id
@app.get("/tasks/{task_id}", status_code=200)
def get_task_by_id(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )



# 3. Create task
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):

    # Handle missing or empty title
    if task.title is None or task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title is required"
        )

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": False
    }

    tasks.append(new_task)

    return new_task



# 4. Update task
@app.put("/tasks/{task_id}", status_code=200)
def update_task(
    task_id: int,
    update: TaskUpdate = Body(...)
):

    # Find task first
    for task in tasks:
        if task["id"] == task_id:

            # Update title only if provided and not empty
            if update.title is not None:
                if update.title.strip() == "":
                    raise HTTPException(
                        status_code=400,
                        detail="Title cannot be empty"
                    )

                task["title"] = update.title


            # Update done if provided
            if update.done is not None:
                task["done"] = update.done


            # If nothing was updated
            if update.title is None and update.done is None:
                raise HTTPException(
                    status_code=400,
                    detail="Empty update body"
                )

            return task


    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )



# 5. Delete task
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):

    for index, task in enumerate(tasks):

        if task["id"] == task_id:
            tasks.pop(index)
            return

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )