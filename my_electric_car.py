from car import Car, ElectricCar

my_tesla = ElectricCar("tesla", "model s", 2019)


print("###### my_electric_car.py ########")
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

