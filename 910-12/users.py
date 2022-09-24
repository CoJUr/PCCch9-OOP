"""A module for storing classes relating to users for exporting purposes."""
from user import User

class Privileges:
    """A simple model of an admin's privileges."""

    def __init__(self, privileges=['can add post', 'can delete post',
                                   'can ban user']):
        """Initialize the attributes. Includes a list of privileges."""
        self.privileges = privileges

    def show_privileges(self):
        """Prints the admins privileges."""
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """A simple model of an Admin class"""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the attributes of the parent class"""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()
