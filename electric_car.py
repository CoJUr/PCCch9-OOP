# class Car:
#     """A simple example of a model of a car"""
#
#     def __init__(self, make, model, year):
#         """Initialize attributes for a car"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """Return a formatted, descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#     def read_odometer(self):
#         """Print a statement revealing the cars current odometer reading"""
#         print(f"This car has {self.odometer_reading} miles on it.")
#
#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value"""
#         self.odometer_reading = mileage
#         """Set the odometer reading to the given value.
#         Reject the change if attempting to rollback.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("Rollback of odometer not allowed.")
#
#     def increment_odometer(self, miles):
#         """Add the given amount to the current odometer reading"""
#         self.odometer_reading += miles
#
#     def fill_gas_tank(self):
#         """Prints a statement indicating the gas tank is now full"""
#         print("The gas tank is full.")
#
#
# class Battery:
#     """A simple attempt to model an electric car battery."""
#
#     def __init__(self, battery_size=75):
#         """Init the battery's attributes"""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """
#         Print a statement describing the battery size.
#         Extracted from ElectricCar class
#         """
#         print(f"This car has a {self.battery_size}-kWh battery.")
#
#     def get_range(self):
#         """Print a statement about the travel range this battery provides."""
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315
#
#         print(f"This car can go about {range} miles on a full charge.")
#
#
# class ElectricCar(Car):
#     """Represents aspects of a car, specific to electric vehicles"""
#
#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         # self.battery_size = 75
#         self.battery = Battery()
#
#     # def describe_battery(self):
#     #     """Print a statement describing the battery size."""
#     #     print(f"This car has a {self.battery_size}-kWh battery.")-snip-
#
#     def fill_gas_tank(self):
#         """Electric cars don't have gas tanks. Overriding parent method."""
#         print("This ELECTRIC car doesn't need a gas tank!")
#
#
# my_tesla = ElectricCar("tesla", "model s", 2019)
# print(my_tesla.get_descriptive_name())
# # my_tesla.describe_battery()
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
#
