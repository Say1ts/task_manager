from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from ..database import (
    get_db,
)
from .service import (
    create_project,
    get_projects,
    get_project,
    update_project,
    delete_project,
)

router = APIRouter(tags=['projects'])


@router.post("/project/")
def create(title: str, description: str, db: Session = Depends(get_db)):
    return create_project(db, title, description)


@router.get("/projects/")
def read_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_projects(db)[skip : skip + limit]


@router.get("/project/{project_id}/")
def read_project(project_id: UUID, db: Session = Depends(get_db)):
    project = get_project(db, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.put("/project/{project_id}/")
def update(
    project_id: UUID,
    title: str = None,
    description: str = None,
    db: Session = Depends(get_db),
):
    project = get_project(db, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return update_project(db, project_id, title, description)


@router.delete("/project/{project_id}/")
def delete(project_id: UUID, db: Session = Depends(get_db)):
    project = get_project(db, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    delete_project(db, project_id)
    return project
