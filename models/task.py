import uuid

class Task:
    def __init__(self, title, assigned_to, project_id, status="incomplete"):
        self.id = str(uuid.uuid4())
        self.title = title
        self.assigned_to = assigned_to  # user_id
        self.project_id = project_id
        self.status = status

    def mark_complete(self):
        self.status = "complete"

    def __repr__(self):
        return f"Task(id={self.id}, title={self.title}, status={self.status}, assigned_to={self.assigned_to}, project_id={self.project_id})"
