from app.models.project import Project


class User:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self._password = password
        self.id = None
        self.projects = []

    @property
    def password(self):
        return None  # Never expose the actual password

    def add_project(self, project):
        if not isinstance(project, Project):
            raise TypeError("Only Project objects can be added to a user")
        self.projects.append(project)
