from ..models import Note  # Предполагается, что модели находятся в файле models.py
from sqlalchemy.orm import Session
from uuid import UUID


def create_note(db: Session, text: str, task_id: UUID):
    note = Note(text=text, task_id=task_id)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


def get_notes(db: Session):
    return db.query(Note).all()


def get_note(db: Session, note_id: UUID):
    return db.query(Note).filter(Note.id == note_id).first()


def update_note(db: Session, note_id: UUID, text: str = None):
    note = get_note(db, note_id)
    if text:
        note.text = text
    db.commit()
    return note


def delete_note(db: Session, note_id: UUID):
    note = get_note(db, note_id)
    db.delete(note)
    db.commit()
