
"""Define the Project class."""


class Project:
    """Represent a project owned by a user."""

    project_count = 0

    def __init__(
        self,
        title,
        description,
        due_date,
        owner_id,
        project_id=None,
    ):
        """Initialize a project with its details and owner."""
        if not title or not title.strip():
            raise ValueError("Project title cannot be empty.")

        Project.project_count += 1
        self.id = project_id or f"project-{Project.project_count}"
        self.title = title.strip()
        self.description = description
        self.due_date = due_date
        self.owner_id = owner_id
        self._tasks = []

    @property
    def tasks(self):
        """Return the tasks associated with this project."""
        return list(self._tasks)

    def add_task(self, task):
        """Add a task to the project if it is not already present."""
        if task not in self._tasks:
            self._tasks.append(task)

    def __str__(self):
        """Return a readable description of the project."""
        return (
            f"{self.title} | Due: {self.due_date} | "
            f"Owner: {self.owner_id}"
        )
