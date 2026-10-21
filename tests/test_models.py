
"""Test the project management model classes."""

import pytest

from models.person import Person
from models.user import User
from models.project import Project
from models.task import Task


def test_person_creation():
    """Check that a person has a name and email."""
    person = Person("Alex", "alex@example.com")
    assert person.name == "Alex"
    assert person.email == "alex@example.com"


def test_person_rejects_invalid_email():
    """Check that invalid emails are rejected."""
    person = Person("Alex", "alex@example.com")

    with pytest.raises(ValueError):
        person.email = "invalid-email"


def test_user_inherits_from_person():
    """Check that User inherits from Person."""
    user = User("Alex", "alex@example.com")
    assert isinstance(user, Person)
    assert user.name == "Alex"


def test_project_creation():
    """Check that a project stores its details."""
    project = Project(
        "CLI Tool",
        "Build a CLI application",
        "2026-12-01",
        "user-1",
    )
    assert project.title == "CLI Tool"
    assert project.owner_id == "user-1"


def test_project_rejects_empty_title():
    """Check that projects need a title."""
    with pytest.raises(ValueError):
        Project("", "Description", "2026-12-01", "user-1")


def test_task_creation():
    """Check that a task starts as Pending."""
    task = Task("Write tests", assigned_to="user-1")
    assert task.status == "Pending"


def test_task_mark_complete():
    """Check that a task can be completed."""
    task = Task("Write tests")
    task.mark_complete()
    assert task.status == "Completed"


def test_task_rejects_invalid_status():
    """Check that invalid task statuses are rejected."""
    with pytest.raises(ValueError):
        Task("Write tests", status="Started")


def test_task_status_setter():
    """Check that a valid status can be updated."""
    task = Task("Write tests")
    task.status = "In Progress"
    assert task.status == "In Progress"


def test_user_can_add_project():
    """Check that a user can own a project."""
    user = User("Alex", "alex@example.com")
    project = Project(
        "CLI Tool",
        "Build a CLI application",
        "2026-12-01",
        user.id,
    )
    user.add_project(project)
    assert project in user.projects


def test_project_can_add_task():
    """Check that a project can contain a task."""
    project = Project(
        "CLI Tool",
        "Build a CLI application",
        "2026-12-01",
        "user-1",
    )
    task = Task("Write tests")
    project.add_task(task)
    assert task in project.tasks


