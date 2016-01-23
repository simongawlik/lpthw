# the number of available cars
cars = 100
# the number of seats in a given car
space_in_a_car = 4.0
# the number of drivers
drivers = 30
# the number of passengers that need transport
passengers = 90
# the numbe of cars that will be idle today
cars_not_driven = cars - drivers
# the number of cars for which drivers are avaialable
cars_driven = drivers
# the number of people that can be transported today
carpool_capacity = cars_driven * space_in_a_car
# the average number of passengers that will travel with each car today
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


# Traceback (most recent call last):
#   File "ex4.py", line 8, in <module>
#     average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined

# This would be an error in line 8. The extra "_" makes the variable something
# that the program does not recognize. To correct it, use "carpool_capacity"
# instead of "car_pool_capacity"

# study drills

# 1. It is not necessary. If you just use 4 the printed number will be 120 
#       instead of 120.0. It also uses integer multiplication.
