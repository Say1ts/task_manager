from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Text, CHAR
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
import uuid

from src.database import engine

Base = declarative_base()


class Project(Base):
    __tablename__ = "project"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    title = Column(Text, nullable=False)
    description = Column(Text)
    timestamp_tz = Column(DateTime(timezone=True), server_default=func.now())


class Task(Base):
    __tablename__ = "task"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    title = Column(Text, nullable=False)
    project_id = Column(UUID(as_uuid=True), ForeignKey("project.id"), nullable=False)
    parent_task = Column(UUID(as_uuid=True), ForeignKey("task.id"), nullable=True)


class Note(Base):
    __tablename__ = "note"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    text = Column(Text, nullable=False)
    task_id = Column(UUID(as_uuid=True), ForeignKey("task.id"), nullable=False)


class User(Base):
    __tablename__ = "user"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    username = Column(CHAR, nullable=False)


class UserProjectPermission(Base):
    __tablename__ = "user_project_permission"

    user_id = Column(
        UUID(as_uuid=True), ForeignKey("user.id"), primary_key=True, nullable=False
    )
    project_id = Column(
        UUID(as_uuid=True), ForeignKey("project.id"), primary_key=True, nullable=False
    )


Base.metadata.create_all(bind=engine)
