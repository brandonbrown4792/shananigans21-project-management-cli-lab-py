import argparse
from utils.file_handler import load_data, save_data, serialize_user, serialize_project, serialize_task
from utils.data_manager import load_users, load_projects, load_tasks
from models.user import User
from models.project import Project
from models.task import Task
from tabulate import tabulate


def main():
    # CLI setup
    parser = argparse.ArgumentParser(description="🛠 Project Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add user
    user_parser = subparsers.add_parser("add-user")
    user_parser.add_argument("--name", required=True)
    user_parser.add_argument("--email", required=True)

    # Add project
    project_parser = subparsers.add_parser("add-project")
    project_parser.add_argument("--user", required=True)
    project_parser.add_argument("--title", required=True)
    project_parser.add_argument("--description", required=True)
    project_parser.add_argument("--due_date", required=True)  # Format: YYYY-MM-DD

    # Add task
    task_parser = subparsers.add_parser("add-task")
    task_parser.add_argument("--project", required=True)
    task_parser.add_argument("--title", required=True)
    task_parser.add_argument("--assigned_to", required=False)

    # Mark task complete
    complete_parser = subparsers.add_parser("complete-task")
    complete_parser.add_argument("--task_id", type=int, required=True)

    # List commands
    subparsers.add_parser("list-users")
    subparsers.add_parser("list-projects")
    subparsers.add_parser("list-tasks")

    # Parse and handle
    args = parser.parse_args()
    data = load_data()
    users = load_users(data)
    projects = load_projects(data, users)
    tasks = load_tasks(data, projects, users)

    if args.command == "add-user":
        user = User(args.name, args.email)
        users[user.id] = user
        data["users"].append(serialize_user(user))
        save_data(data)
        print(f"User '{user.name}' added.")

    elif args.command == "add-project":
        user = next((u for u in users.values() if u.name == args.user), None)
        if not user:
            print("User not found.")
            return
        project = Project(args.title, args.description, args.due_date)
        user.add_project(project)
        projects[project.id] = project
        data["projects"].append(serialize_project(project))
        save_data(data)
        print(f"Project '{project.title}' added for user '{user.name}'.")

    elif args.command == "add-task":
        project = next((p for p in projects.values() if p.title == args.project), None)
        if not project:
            print("Project not found.")
            return
        assigned_user = next((u for u in users.values() if u.name == args.assigned_to), None) if args.assigned_to else None
        task = Task(args.title, assigned_to=assigned_user)
        project.add_task(task)
        tasks[task.id] = task
        data["tasks"].append(serialize_task(task))
        save_data(data)
        print(f"Task '{task.title}' added to project '{project.title}'.")

    elif args.command == "complete-task":
        task = tasks.get(args.task_id)
        if not task:
            print("Task ID not found.")
            return
        task.mark_complete()
        # Re-serialize all tasks
        data["tasks"] = [serialize_task(t) for t in tasks.values()]
        save_data(data)
        print(f"Task '{task.title}' marked complete.")

    elif args.command == "list-users":
        for user in users.values():
            print(user)

    elif args.command == "list-projects":
        for project in projects.values():
            print(project)

    elif args.command == "list-tasks":
        for task in tasks.values():
            print(task)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
