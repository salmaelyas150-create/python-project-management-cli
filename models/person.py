
"""Define the base Person class."""


class Person:
    """Represent a person in the project management system."""

    def __init__(self, name, email):
        """Initialize a person with a name and email address."""
        self.name = name
        self._email = email

    @property
    def email(self):
        """Return the person's email address."""
        return self._email

    @email.setter
    def email(self, value):
        """Validate and update the person's email address."""
        if not isinstance(value, str) or "@" not in value:
            raise ValueError("Please provide a valid email address.")
        self._email = value

    def __str__(self):
        """Return a readable description of the person."""
        return f"{self.name} ({self.email})"
