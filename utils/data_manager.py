from models.user import User
from models.project import Project
from models.task import Task

def load_users(data):
    users = {}
    for u in data["users"]:
        user = User(u["name"], u["email"])
        user.id = u["id"]
        users[user.id] = user
    # User.id_counter = max(users.keys(), default=0) + 1 # This doesn't work because the user key is a string. Honestly, this is not needed at all.
    return users

def load_projects(data, users):
    projects = {}
    for p in data["projects"]:
        project = Project(p["title"], p["description"], p["due_date"], p["user_id"]) # Missing user_id here
        project.id = p["id"]
        projects[project.id] = project
        # Assign to user (reverse lookup)
        for user in users.values():
            if project.id in p.get("projects", []) or project.id in [pr.id for pr in user.projects]:
                user.add_project(project)
                break
    # Project.id_counter = max(projects.keys(), default=0) + 1 # This not needed either
    return projects

def load_tasks(data):
    tasks = {}
    for t in data["tasks"]:
    #     assigned_user = users.get(t["assigned_to"])
    #     task = Task(t["title"], assigned_to=assigned_user)
    #     task.id = t["id"]
    #     task.status = t["status"]
    #     tasks[task.id] = task
    #     # Attach task to project
    #     for project in projects.values():
    #         if task.id in t.get("tasks", []) or task.id in [tsk.id for tsk in project.tasks]:
    #             project.add_task(task)
    #             break
    # Task.id_counter = max(tasks.keys(), default=0) + 1

        # Here we can just load the tasks straight from the data. No need for projects or tasks
        tasks[t['id']] = Task(t['title'], t['assigned_to'], t['project_id'], t['status'], t['id'])
    return tasks
