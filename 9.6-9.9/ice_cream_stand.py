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


my_restaurant = Restaurant('The Blue Plate', 'American')
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


class IceCreamStand (Restaurant):
    """A simple model of an ice cream stand type of Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def display_flavors(self):
        """Prints a list of the available icecream flavors"""
        print(f"The flavors at {self.restaurant_name} are: {self.flavors}")


my_icecream_stand = IceCreamStand("Baskin Robbins", "Ice Cream")
my_icecream_stand.display_flavors()




