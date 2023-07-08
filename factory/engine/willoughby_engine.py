from engine.engine import Engine

# Willoughby Engine class implements Engine Interface
class WilloughbyEngine(Engine):

    # Constructor
    def __init__(self, last_service_mileage, current_mileage):
        self.__last_service_mileage = last_service_mileage
        self.__current_mileage = current_mileage
    
    # Implementing needs_service() method from Engine interface
    def needs_service(self):
        return self.__current_mileage - self.__last_service_mileage > 60000