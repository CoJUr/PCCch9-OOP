# from car import Car, ElectricCar
#
# print("###### my_car.py ########")
# my_beetle = Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = ElectricCar("tesla", "roadster", 2019)
# print(my_tesla.get_descriptive_name())


# could also import entire car module and use dot notation to access needed
# classes. *Preferred approach when needing many of a modules classes*
from car import Car
from electric_car import ElectricCar as EC

print("###### my_carS.py ########")

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = EC("tesla", "roadster", 2019)
print(my_tesla.get_descriptive_name())

