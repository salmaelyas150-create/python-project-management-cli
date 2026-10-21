
"""Define the User class."""

from models.person import Person


class User(Person):
    """Represent a user who can own projects and contribute to tasks."""

    user_count = 0

    def __init__(self, name, email, user_id=None):
        """Initialize a user and assign a unique identifier."""
        super().__init__(name, email)
        User.user_count += 1
        self.id = user_id or f"user-{User.user_count}"
        self._projects = []

    @property
    def projects(self):
        """Return the projects belonging to this user."""
        return list(self._projects)

    def add_project(self, project):
        """Add a project to this user's project collection."""
        if project not in self._projects:
            self._projects.append(project)

    def __str__(self):
        """Return a readable description of the user."""
        return f"{self.name} | {self.email} | ID: {self.id}"


