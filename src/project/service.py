from sqlalchemy.orm import Session
from uuid import UUID
from ..models import Project


def create_project(db: Session, title: str, description: str):
    project = Project(title=title, description=description)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get_projects(db: Session):
    return db.query(Project).all()


def get_project(db: Session, project_id: UUID):
    return db.query(Project).filter(Project.id == project_id).first()


def update_project(
    db: Session, project_id: UUID, title: str = None, description: str = None
):
    project = get_project(db, project_id)
    if title:
        project.title = title
    if description:
        project.description = description
    db.commit()
    return project


def delete_project(db: Session, project_id: UUID):
    project = get_project(db, project_id)
    db.delete(project)
    db.commit()
