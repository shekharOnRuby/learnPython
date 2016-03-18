#Number of cars.
cars = 100
#Seats available in a car.
space_in_a_car = 4.0

# nuumber of drivers available in a car.
drivers = 30

#Numbers of passengers needing transportation.
passengers = 90

#Deducing how many cars are empty.
cars_not_driven = cars - drivers

#how many cars can be driven? that will be determined by number of drivers available.
cars_driven = drivers

#deducing the number of passengers for a carpool
carpool_capacity = cars_driven * space_in_a_car

#Efficient carpool capacity.
average_passengers_per_car = passengers / cars_driven

print "There are ", cars,"cars available."
print "There are only ", drivers," drivers available."
print "There will be ", cars_not_driven, " empty cars today."
print "We can transport ", carpool_capacity," people today."
print "We have ",passengers," to carpool today."
print "We need to put about", average_passengers_per_car, " in each car."
