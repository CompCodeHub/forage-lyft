from tire.tire import Tire

# Octoprime Tire class implements Tire interface
class OctoprimeTire(Tire):

    # Constructor
    def __init__(self, tire_sensor_data):
        self.__tire_sensor_data = tire_sensor_data
    
    # Implementing needs_service() method from Tire interface
    def needs_service(self):
        return sum(self.__tire_sensor_data) >= 3