from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

from ..database import (
    get_db,
)
from .service import (
    create_task,
    get_tasks,
    get_task,
    update_task,
    delete_task,
)

router = APIRouter(tags=['task'])


@router.post("/task/")
def create(
    title: str,
    project_id: UUID,
    parent_task: UUID = None,
    db: Session = Depends(get_db),
):
    return create_task(db, title, project_id, parent_task)


@router.get("/tasks/")
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_tasks(db)[skip : skip + limit]


@router.get("/task/{task_id}/")
def read_task(task_id: UUID, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/task/{task_id}/")
def update(
    task_id: UUID,
    title: str = None,
    parent_task: UUID = None,
    db: Session = Depends(get_db),
):
    task = get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return update_task(db, task_id, title, parent_task)


@router.delete("/task/{task_id}/")
def delete(task_id: UUID, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    delete_task(db, task_id)
    return task
