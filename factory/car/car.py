from interface.serviceable import Serviceable

# Car class implements serviceable interface
class Car(Serviceable):

    # Constructor
    def __init__(self, engine, battery, tire_data):
        self.__engine = engine
        self.__battery = battery
        self.__tire_data = tire_data

    # Implementing method from serviceable interface
    def needs_service(self):
        return self.__engine.needs_service() or self.__battery.needs_service() or self.__tire_data.needs_service()