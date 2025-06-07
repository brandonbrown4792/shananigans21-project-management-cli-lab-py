import uuid

class Project:
    def __init__(self, title, description, due_date, user_id):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.due_date = due_date
        self.user_id = user_id

    def __repr__(self):
        return f"Project(id={self.id}, title={self.title}, due_date={self.due_date}, user_id={self.user_id})"
