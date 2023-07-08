from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
from car.car import Car

# Car Factory class
class CarFactory:
    
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(tire_sensor_data)
        car = Car(engine, battery, tire)
        return car
    

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(tire_sensor_data)
        car = Car(engine, battery, tire)
        return car
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_sensor_data):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_sensor_data)
        car = Car(engine, battery, tire)
        return car
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_sensor_data)
        car = Car(engine, battery, tire)
        return car
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor_data):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_sensor_data)
        car = Car(engine, battery, tire)
        return car
    
    
    
