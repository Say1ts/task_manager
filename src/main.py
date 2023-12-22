from fastapi import FastAPI
from .note.router import router as note_router
from .project.router import router as project_router
from .task.router import router as task_router

app = FastAPI()

app.include_router(note_router, prefix="/api/v1")
app.include_router(task_router, prefix="/api/v1")
app.include_router(project_router, prefix="/api/v1")
