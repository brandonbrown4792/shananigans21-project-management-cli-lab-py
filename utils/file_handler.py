import json
import os

DATA_PATH = "data/data.json"

def load_data():
    """Load and return the full dataset from the JSON file."""
    if not os.path.exists(DATA_PATH):
        return {"users": [], "projects": [], "tasks": []}
    
    try:
        with open(DATA_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Warning: Malformed JSON. Starting with empty data.")
        return {"users": [], "projects": [], "tasks": []}

def save_data(data):
    """Write the entire data dictionary to the JSON file."""
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=4, default=str)  # Default=str for datetime serialization

# Still inside utils/file_handler.py

def serialize_user(user):
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "projects": [p.id for p in user.projects]
    }

def serialize_project(project):
    return {
        "id": project.id,
        "title": project.title,
        "description": project.description,
        "due_date": project.due_date.strftime("%Y-%m-%d"),
        "tasks": [t.id for t in project.tasks]
    }

def serialize_task(task):
    return {
        "id": task.id,
        "title": task.title,
        "status": task.status,
        "assigned_to": task.assigned_to.id if task.assigned_to else None
    }
