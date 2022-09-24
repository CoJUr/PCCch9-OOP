"""A set of classes for representing gas and electric cars"""


class Car:
    """A simple example of a model of a car"""

    def __init__(self, make, model, year):
        """Initialize attributes for a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a formatted, descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement revealing the cars current odometer reading"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value"""
        self.odometer_reading = mileage
        """Set the odometer reading to the given value.
        Reject the change if attempting to rollback. 
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Rollback of odometer not allowed.")

    #        now update only goes thru if arg >= current state

    def increment_odometer(self, miles):
        """Add the given amount to the current odometer reading"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Prints a statement indicating the gas tank is now full"""
        print("The gas tank is full.")

