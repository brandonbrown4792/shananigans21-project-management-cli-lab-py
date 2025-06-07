# models/user.py
import uuid

class User:
    def __init__(self, name, email):
        self.id = str(uuid.uuid4())  # Unique user ID
        self.name = name
        self.email = email
        self.projects = []  #Store user's projects in memory

    def add_project(self, project):
        """Assign a project to this user."""
        self.projects.append(project)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"
