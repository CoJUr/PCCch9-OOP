class Restaurant:
    """A simple model of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints the two attributes of the restaurant"""
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Prints a message that the restaurant is open"""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        """Updates the number of customers served as per number_served"""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """Increments the number of customers served by passed value"""
        self.number_served += number_served

my_restaurant = Restaurant('The Blue Plate', 'American')
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print("####")
restaurant = Restaurant('Don\'s', 'Italian')
print(restaurant.number_served)
restaurant.number_served = 5
print(restaurant.number_served)

print("####\n directly updating number served via method:")
restaurant.set_number_served(10)
print(restaurant.number_served)

print("####\n incrementing number served via increment_number_served:")
restaurant.increment_number_served(24)
print(f"{restaurant.number_served} customers have now been served.")