# used_cars.py

from car import Car

# Create a new Car object called "limo" that is initialised with 100 units of fuel.
limo = Car(100)

# Add 20 more units of fuel to this new car object using the add method.
limo.add_fuel(20)

# Print the amount of fuel in the car.
print(f"The amount of fuel in the car: {limo.fuel}")

# Attempt to drive the car 115 km using the drive method.
distance_driven = limo.drive(115)
print(f"The car drove {distance_driven} km")

# Print the car object to ensure that the __str__ method is working as expected.
print(limo)
