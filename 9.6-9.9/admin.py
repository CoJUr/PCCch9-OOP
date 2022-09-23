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
print("#######")
user_3.describe_user()
user_3.greet_user()


class Privileges:
    """A simple model of an admin's privileges."""

    def __init__(self, privileges=['can add post', 'can delete post',
                                   'can ban user']):
        """Initialize the attributes. Includes a list of privileges."""
        self.privileges = privileges

    def show_privileges(self):
        """Prints the admin's privileges."""
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """A simple model of an Admin class"""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the attributes of the parent class"""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()


admin_1 = Admin('joe', 'smith', 'jsmith', 'joey@gmail.com', "New York, NY")
print(admin_1.privileges.show_privileges())
