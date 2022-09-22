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


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())


# three ways to modify an attribute value: directly | method+/-incrementally


# 1. Directly modify the value of an attribute
print("#######")
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# 2. Modify the value of an attribute via a method
print("#######\n via method")
my_new_car.update_odometer(25)
my_new_car.read_odometer()

# 3. Increment the value of an attribute via a method
print("\n INCREMENTING via method:")
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

