from interface.serviceable import Serviceable

# Car class implements serviceable interface
class Car(Serviceable):

    # Constructor
    def __init__(self, engine, battery):
        self.__engine = engine
        self.__battery = battery

    # Implementing method from serviceable interface
    def needs_service(self):
        return self.__engine.needs_service() or self.__battery.needs_service()