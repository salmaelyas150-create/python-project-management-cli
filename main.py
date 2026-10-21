
"""Command-line project management application."""

import argparse

from rich.console import Console
from rich.table import Table

from utils.storage import load_data, save_data

console = Console()


def add_user(args):
    """Create and save a user."""
    users = load_data("users")

    if any(user["email"].lower() == args.email.lower() for user in users):
        console.print("[red]A user with that email already exists.[/red]")
        return

    user = {
        "id": f"user-{len(users) + 1}",
        "name": args.name,
        "email": args.email,
    }

    users.append(user)
    save_data("users", users)
    console.print(f"[green]Created user:[/green] {user['name']} ({user['id']})")


def list_users(args):
    """Display all registered users."""
    users = load_data("users")

    if not users:
        console.print("[yellow]No users found.[/yellow]")
        return

    table = Table(title="Users")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Email")

    for user in users:
        table.add_row(user["id"], user["name"], user["email"])

    console.print(table)


def add_project(args):
    """Create a project belonging to an existing user."""
    users = load_data("users")
    projects = load_data("projects")

    owner = next(
        (
            user for user in users
            if user["name"].lower() == args.user.lower()
            or user["id"].lower() == args.user.lower()
        ),
        None,
    )

    if owner is None:
        console.print("[red]User not found. Create the user first.[/red]")
        return

    project = {
        "id": f"project-{len(projects) + 1}",
        "title": args.title,
        "description": args.description,
        "due_date": args.due_date,
        "owner_id": owner["id"],
    }

    projects.append(project)
    save_data("projects", projects)
    console.print(
        f"[green]Created project:[/green] {project['title']} "
        f"({project['id']})"
    )


def list_projects(args):
    """Display projects, optionally filtered by user."""
    projects = load_data("projects")
    users = load_data("users")

    if args.user:
        matching_users = [
            user for user in users
            if user["name"].lower() == args.user.lower()
            or user["id"].lower() == args.user.lower()
        ]
        matching_ids = {user["id"] for user in matching_users}
        projects = [
            project for project in projects
            if project["owner_id"] in matching_ids
        ]

    if not projects:
        console.print("[yellow]No matching projects found.[/yellow]")
        return

    table = Table(title="Projects")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Description")
    table.add_column("Due date")
    table.add_column("Owner")

    for project in projects:
        table.add_row(
            project["id"],
            project["title"],
            project["description"],
            project["due_date"],
            project["owner_id"],
        )

    console.print(table)


def add_task(args):
    """Create a task belonging to an existing project."""
    projects = load_data("projects")
    tasks = load_data("tasks")
    users = load_data("users")

    project = next(
        (
            item for item in projects
            if item["title"].lower() == args.project.lower()
            or item["id"].lower() == args.project.lower()
        ),
        None,
    )

    if project is None:
        console.print("[red]Project not found. Create it first.[/red]")
        return

    assigned_to = None

    if args.assigned_to:
        user = next(
            (
                item for item in users
                if item["name"].lower() == args.assigned_to.lower()
                or item["id"].lower() == args.assigned_to.lower()
            ),
            None,
        )

        if user is None:
            console.print("[red]Assigned user not found.[/red]")
            return

        assigned_to = user["id"]

    task = {
        "id": f"task-{len(tasks) + 1}",
        "title": args.title,
        "status": "Pending",
        "assigned_to": assigned_to,
        "project_id": project["id"],
    }

    tasks.append(task)
    save_data("tasks", tasks)
    console.print(
        f"[green]Created task:[/green] {task['title']} ({task['id']})"
    )


def list_tasks(args):
    """Display tasks, optionally filtered by project."""
    tasks = load_data("tasks")

    if args.project:
        projects = load_data("projects")
        project = next(
            (
                item for item in projects
                if item["title"].lower() == args.project.lower()
                or item["id"].lower() == args.project.lower()
            ),
            None,
        )

        if project is None:
            console.print("[red]Project not found.[/red]")
            return

        tasks = [
            task for task in tasks
            if task["project_id"] == project["id"]
        ]

    if not tasks:
        console.print("[yellow]No matching tasks found.[/yellow]")
        return

    table = Table(title="Tasks")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Status")
    table.add_column("Assigned to")
    table.add_column("Project")

    for task in tasks:
        table.add_row(
            task["id"],
            task["title"],
            task["status"],
            task["assigned_to"] or "Nobody",
            task["project_id"],
        )

    console.print(table)


def complete_task(args):
    """Mark an existing task as completed."""
    tasks = load_data("tasks")

    task = next(
        (
            item for item in tasks
            if item["id"].lower() == args.id.lower()
        ),
        None,
    )

    if task is None:
        console.print("[red]Task not found.[/red]")
        return

    task["status"] = "Completed"
    save_data("tasks", tasks)
    console.print(f"[green]Completed task:[/green] {task['title']}")


def build_parser():
    """Create the argument parser and its subcommands."""
    parser = argparse.ArgumentParser(
        description="Manage users, projects, and tasks."
    )
    commands = parser.add_subparsers(dest="command", required=True)

    command = commands.add_parser("add-user", help="Create a user")
    command.add_argument("--name", required=True)
    command.add_argument("--email", required=True)
    command.set_defaults(func=add_user)

    command = commands.add_parser("list-users", help="List users")
    command.set_defaults(func=list_users)

    command = commands.add_parser("add-project", help="Create a project")
    command.add_argument("--user", required=True, help="Owner name or ID")
    command.add_argument("--title", required=True)
    command.add_argument("--description", default="No description")
    command.add_argument("--due-date", dest="due_date", required=True)
    command.set_defaults(func=add_project)

    command = commands.add_parser("list-projects", help="List projects")
    command.add_argument("--user", help="Filter by user name or ID")
    command.set_defaults(func=list_projects)

    command = commands.add_parser("add-task", help="Create a task")
    command.add_argument("--project", required=True, help="Project title or ID")
    command.add_argument("--title", required=True)
    command.add_argument("--assigned-to", dest="assigned_to")
    command.set_defaults(func=add_task)

    command = commands.add_parser("list-tasks", help="List tasks")
    command.add_argument("--project", help="Filter by project title or ID")
    command.set_defaults(func=list_tasks)

    command = commands.add_parser(
        "complete-task", help="Mark a task as completed"
    )
    command.add_argument("--id", required=True, help="Task ID")
    command.set_defaults(func=complete_task)

    return parser


def main():
    """Parse command-line arguments and run the selected command."""
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
