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
        print(f"{self.first_name} {self.last_name} is from {self.location}."
              f"\n{self.first_name} can be reached at {self.email}."
              f"\n{self.first_name}'s username is {self.username}.")

    def greet_user(self):
        """Prints a personalized greeting to the user"""
        print(f"Hello {self.first_name} {self.last_name}!")


user_1 = User('joe', 'smith', 'jsmith', 'jsmith@email.com',
              'New York, NY')

user_2 = User('jane', 'doe', 'jdoe', 'jdoe@email.com',
              'Los Angeles, CA')

user_3 = User('jim', 'smith', 'jsmith', 'jsmith@email.com',
              'Chicago, IL')

user_1.describe_user()
user_1.greet_user()
print("#######")
user_2.describe_user()
user_2.greet_user()
