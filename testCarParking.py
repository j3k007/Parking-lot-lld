import unittest
from ParkingLot import Garage, Car

class TestParingLot(unittest.TestCase):

    def test_spots_available(self):
        my_garage = Garage()
        self.assertEqual(my_garage.spot_available(), 20)

    def test_add_car(self):
        my_garage = Garage()
        self.assertEqual(my_garage.add_car(Car('UHGD6', 'Corolla','Pink')), 
                         "car successfully added to the parking lot")
        
    def test_remove_car(self):
        my_garage = Garage()
        my_garage.add_car(Car('UHGD6', 'Corolla', 'Pink'))
        self.assertEqual(my_garage.remove_car('A1', '5'), 'Your total bill is $25')