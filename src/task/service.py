from sqlalchemy import UUID
from sqlalchemy.orm import Session

from ..models import Task  # Предполагается, что модели находятся в файле models.py


def create_task(db: Session, title: str, project_id: UUID, parent_task: UUID = None):
    task = Task(title=title, project_id=project_id, parent_task=parent_task)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks(db: Session):
    return db.query(Task).all()


def get_task(db: Session, task_id: UUID):
    return db.query(Task).filter(Task.id == task_id).first()


def update_task(
    db: Session, task_id: UUID, title: str = None, parent_task: UUID = None
):
    task = get_task(db, task_id)
    if title:
        task.title = title
    if parent_task:
        task.parent_task = parent_task
    db.commit()
    return task


def delete_task(db: Session, task_id: UUID):
    task = get_task(db, task_id)
    db.delete(task)
    db.commit()
