
"""Define the Task class."""


class Task:
    """Represent a task belonging to a project."""

    task_count = 0
    VALID_STATUSES = ("Pending", "In Progress", "Completed")

    def __init__(
        self,
        title,
        status="Pending",
        assigned_to=None,
        task_id=None,
    ):
        """Initialize a task with a title, status, and assignee."""
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty.")

        if status not in self.VALID_STATUSES:
            raise ValueError(
                f"Status must be one of {self.VALID_STATUSES}."
            )

        Task.task_count += 1
        self.id = task_id or f"task-{Task.task_count}"
        self.title = title.strip()
        self._status = status
        self.assigned_to = assigned_to

    @property
    def status(self):
        """Return the current task status."""
        return self._status

    @status.setter
    def status(self, value):
        """Update the status only when it is valid."""
        if value not in self.VALID_STATUSES:
            raise ValueError(
                f"Status must be one of {self.VALID_STATUSES}."
            )
        self._status = value

    def mark_complete(self):
        """Mark the task as completed."""
        self.status = "Completed"

    def __str__(self):
        """Return a readable description of the task."""
        return (
            f"{self.title} | {self.status} | "
            f"Assigned to: {self.assigned_to or 'Nobody'}"
        )
