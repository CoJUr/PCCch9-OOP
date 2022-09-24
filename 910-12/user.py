class User:
    """A simple model of a User class"""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        """Prints a summary of the user's information"""
        print(f"{self.first_name.title()} {self.last_name.title()} is from"
              f" {self.location}."
              f"\n{self.first_name.title()} can be reached at {self.email}."
              f"\n{self.first_name.title()}'s username is {self.username}.")

    def greet_user(self):
        """Prints a personalized greeting to the user"""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!")
