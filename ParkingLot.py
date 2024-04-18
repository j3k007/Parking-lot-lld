# Defining the car class
class Car:

    # Class constructor
    def __init__(self, license_plate: str, model: str, color: str) -> None:
        self.license_plate = license_plate
        self.model = model
        self.color = color

    # Method to print Car details.
    def __repr__(self) -> str:
        return f"{self.license_plate}, {self.model}, {self.color}"
    
class Garage:

    # Constructor for Garage Class
    def __init__(self) -> None:
        self.cars_added = []
        self.spots = 20
        self.car_info = {}
        self.bill = 0

    # Returns number of Spots available
    def spot_available(self):
        return self.spots
    
    # Add car function to add the car into Parking lot, It takes one input parameter that is license_plate, model, car.
    def add_car(self, car):
        self.identifier = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1', 'K1', 'L1', 'M1', 'N1', 'O1', 'P1', 'Q1', 'R1', 'S1', 'T1']
        if self.spots > 0:
            self.cars_added.append(str(car).split(', '))
            self.spots -= 1
            self.car_info = {'code':[], 'license_plate':[], 'Model':[], 'Color':[]}

            for index, i in enumerate(self.cars_added):
                self.car_info['code'].append(self.identifier[index])
                self.car_info['license_plate'].append(i[0])
                self.car_info['Model'].append(i[1])
                self.car_info['Color'].append(i[2])
            return f"Car successfully added to the parking lot."

        else:
            print(f"We have {self.spot_available} spots available. I am sorry.")
        
    def remove_car(self, given_code, bill_hours):
        past_len = len(self.car_info['code'])

        if given_code not in self.car_info['code']:
            print("We could not find you car. Are you sure you parked your car here ?")
        else:
            for index, value in enumerate(self.car_info['code']):
                if value == given_code:
                    print(f"License Plate: {self.car_info['license_plate'][index]}")
                    print(f"Car's Model: {self.car_info['Model'][index]}")
                    print(f"Car's Color: {self.car_info['Color'][index]}")

                    remove_cars_index = self.car_info['code'].pop(index)
                    self.car_info['license_plate'].pop(index)
                    self.car_info['Model'].pop(index)
                    self.car_info['Color'].pop(index)

                    self.spots += 1
        
        if len(self.car_info['code']) < past_len:
            while True:
                if bill_hours.isnumeric():
                    list_of_time_and_code = [bill_hours, remove_cars_index]
                    break
                else:
                    print("Your input must be an integer. Sample input: 5")
                bill_hours = input("From how long your were in the parking lot in hours or 'q' to quit. Example input: 5")
                if bill_hours in ['q', 'Q']:
                    break

            if int(list_of_time_and_code[0]) < 20:
                self.bill = int(list_of_time_and_code[0]) * 5
                return f"Your total bill is ${self.bill}"
            else:
                self.bill =  int(list_of_time_and_code[0]) * 5 + 100
                return f"Your total bill with fine is ${self.bill}"

    def cars_in_parking(self):
        for i in self.car_info.items():
            print(i)

my_garage = Garage()
print(my_garage.spot_available())
my_garage.add_car(Car('LVG34', 'Ferrari', 'Red'))
my_garage.add_car(Car('UTEV3', 'Porsche', 'Blue'))
my_garage.add_car(Car('LVG34', 'Optra', 'Red'))
my_garage.cars_in_parking()
print(my_garage.remove_car('A1', '10'))
print(my_garage.spot_available())
