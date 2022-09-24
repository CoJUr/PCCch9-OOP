class Restaurant:
    """A simple model of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the two attributes of the restaurant"""
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Prints a message that the restaurant is open"""
        print(f"{self.restaurant_name} is now open!")