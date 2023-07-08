from tire.tire import Tire

# Carrigan Tire class implements Tire interface
class CarriganTire(Tire):

    # Constructor
    def __init__(self, tire_sensor_data):
        self.__tire_sensor_data = tire_sensor_data

    # Implementing needs_service() method from Tire interface
    def needs_service(self):
        for value in self.__tire_sensor_data:
            if value >= 0.9:
                return True
        
        return False