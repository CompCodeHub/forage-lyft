import unittest
from datetime import datetime

import sys
sys.path.insert(0, 'factory')

from car_factory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        current_mileage = 30001
        last_service_mileage = 0
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertFalse(car.needs_service())
    
    def test_tire_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = [0.2, 0.4, 0.9, 0.1]

        car_factory = CarFactory()
        car = car_factory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertTrue(car.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = [0.2, 0.4, 0.8, 0.1]

        car_factory = CarFactory()
        car = car_factory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        curent_date = datetime.today().date()
        last_service_date = curent_date.replace(year=curent_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_glissade(curent_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        curent_date = datetime.today().date()
        last_service_date = curent_date
        current_mileage = 60001
        last_service_mileage = 0
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_glissade(curent_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        curent_date = datetime.today().date()
        last_service_date = curent_date
        current_mileage = 60000
        last_service_mileage = 0
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_glissade(curent_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertFalse(car.needs_service())
    
    def test_tire_should_be_serviced(self):
        curent_date = datetime.today().date()
        last_service_date = curent_date
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.3, 0.9, 0.6]

        car_factory = CarFactory()
        car = car_factory.create_glissade(curent_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertTrue(car.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        curent_date = datetime.today().date()
        last_service_date = curent_date
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.3, 0.8, 0.6]

        car_factory = CarFactory()
        car = car_factory.create_glissade(curent_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        warning_light_is_on = False
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_palindrome(current_date, last_service_date, warning_light_is_on, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        warning_light_is_on = False
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_palindrome(current_date, last_service_date, warning_light_is_on, tire_sensor_data)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        warning_light_is_on = True
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_palindrome(current_date, last_service_date, warning_light_is_on, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        warning_light_is_on = False
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_palindrome(current_date, last_service_date, warning_light_is_on, tire_sensor_data)
        self.assertFalse(car.needs_service())
    
    def test_tire_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        warning_light_is_on = False
        tire_sensor_data = [0.9, 0.9, 0.6, 0.6]

        car_factory = CarFactory()
        car = car_factory.create_palindrome(current_date, last_service_date, warning_light_is_on, tire_sensor_data)
        self.assertTrue(car.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        warning_light_is_on = False
        tire_sensor_data = [0.9, 0.7, 0.6, 0.6]

        car_factory = CarFactory()
        car = car_factory.create_palindrome(current_date, last_service_date, warning_light_is_on, tire_sensor_data)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        curent_date = datetime.today().date()
        last_service_date = curent_date.replace(year=curent_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_rorschach(curent_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        curent_date = datetime.today().date()
        last_service_date = curent_date.replace(year=curent_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_rorschach(curent_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        current_mileage = 60001
        last_service_mileage = 0
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        current_mileage = 60000
        last_service_mileage = 0
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        current_mileage = 60000
        last_service_mileage = 0
        tire_sensor_data = [0.9, 0.8, 0.9, 0.8]

        car_factory = CarFactory()
        car = car_factory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertTrue(car.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        current_mileage = 60000
        last_service_mileage = 0
        tire_sensor_data = [0.9, 0.2, 0.9, 0.8]

        car_factory = CarFactory()
        car = car_factory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertFalse(car.needs_service())

class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        current_mileage = 30001
        last_service_mileage = 0
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_data = []

        car_factory = CarFactory()
        car = car_factory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertFalse(car.needs_service())
    
    def test_tire_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_data = [0.9, 0.8, 0.9, 0.8]

        car_factory = CarFactory()
        car = car_factory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertTrue(car.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_data = [0.9, 0.3, 0.2, 0.8]

        car_factory = CarFactory()
        car = car_factory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
