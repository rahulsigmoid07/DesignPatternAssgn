# Factory Design Pattern: Vehicle Manufacturing System
from abc import ABC, abstractmethod
# Abstract Vehicle
class Vehicle(ABC):
    def __init__(self):
        self.num_wheels = 0
        self.seating_capacity = 0
        self.max_speed = 0

    def display_details(self):
        pass


# Concrete Vehicles
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.num_wheels = 4
        self.seating_capacity = 5
        self.max_speed = 200

    def display_details(self):
        print("Car - Number of Wheels: {}, Seating Capacity: {}, Max Speed: {}"
              .format(self.num_wheels, self.seating_capacity, self.max_speed))


class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__()
        self.num_wheels = 2
        self.seating_capacity = 2
        self.max_speed = 180

    def display_details(self):
        print("Motorcycle - Number of Wheels: {}, Seating Capacity: {}, Max Speed: {}"
              .format(self.num_wheels, self.seating_capacity, self.max_speed))


class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.num_wheels = 6
        self.seating_capacity = 3
        self.max_speed = 150

    def display_details(self):
        print("Truck - Number of Wheels: {}, Seating Capacity: {}, Max Speed: {}"
              .format(self.num_wheels, self.seating_capacity, self.max_speed))


# Vehicle Factory
class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "motorcycle":
            return Motorcycle()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError("Invalid vehicle type.")


# Usage example
if __name__ == "__main__":
    # Create vehicle factory object
    factory = VehicleFactory()

    # Manufacture a car
    car = factory.create_vehicle("car")
    car.display_details()

    # Manufacture a motorcycle
    motorcycle = factory.create_vehicle("motorcycle")
    motorcycle.display_details()

    # Manufacture a truck
    truck = factory.create_vehicle("truck")
    truck.display_details()
