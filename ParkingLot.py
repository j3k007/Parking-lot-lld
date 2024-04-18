# Defining the car class
class Car:

    # Class constructor
    def __init__(self, license_plate: str, model: str, color: str) -> None:
        self.license_plate = license_plate
        self.model = model
        self.color = color