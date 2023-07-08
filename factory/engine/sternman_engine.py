from engine.engine import Engine

# Sternman Engine class implements Engine Interface
class SternmanEngine(Engine):

    # Constructor
    def __init__(self, warning_light_on):
        self.__warning_light_on = warning_light_on
    
    # Implementing needs_service() method from Engine interface
    def needs_service(self):
        return self.__warning_light_on