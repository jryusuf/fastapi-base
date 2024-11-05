import uuid
from app.models.source import Source


class Project:
    VALID_STATUSES = ['RUNNING', 'STOPPED', 'PAUSED']

    def __init__(self, name: str, status: str = 'STOPPED'):
        self.name = name
        self.sources = []
        self.status = status
        self.id = uuid.uuid4()  # Generate a unique UUID for each project

    def add_source(self, source):
        if not isinstance(source, Source):
            raise TypeError("Only Source objects can be added to a project")
        self.sources.append(source)

    def update_status(self, new_status: str):
        if new_status not in self.VALID_STATUSES:
            raise ValueError("Invalid project status")
        self.status = new_status
