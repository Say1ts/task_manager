from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from .service import create_note, get_notes, get_note, update_note, delete_note
from ..database import (
    get_db,
)


router = APIRouter(tags=["notes"])


@router.post("/note/")
def create(text: str, task_id: UUID, db: Session = Depends(get_db)):
    return create_note(db, text, task_id)


@router.get("/notes/")
def read_notes(db: Session = Depends(get_db)):
    return get_notes(db)


@router.get("/note/{note_id}")
def read_note(note_id: UUID, db: Session = Depends(get_db)):
    return get_note(db, note_id)


@router.put("/note/{note_id}")
def update(note_id: UUID, text: str, db: Session = Depends(get_db)):
    return update_note(db, note_id, text)


@router.delete("/note/{note_id}")
def delete(note_id: UUID, db: Session = Depends(get_db)):
    delete_note(db, note_id)
    return {"status": "note deleted"}
