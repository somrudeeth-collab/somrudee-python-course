""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return (
            f"Vehicle info:\n"
            f"Brand: {self.brand}\n"
            f"Model: {self.model}\n"
            f"Year: {self.year}"
        )


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return (
            f"{super().get_info()}\n"
            f"Number of doors: {self.number_of_doors}"
        )


# Create a Vehicle object
vehicle = Vehicle("Toyota", "Yaris", 2025)
print(vehicle.get_info())

print()

# Create a Car object
car = Car("Honda", "Civic", 2024, 4)
print(car.get_info())