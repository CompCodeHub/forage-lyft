from battery.battery import Battery

# Spindler Battery class implements Battery interface
class SpindlerBattery(Battery):

    # Constructor
    def __init__(self, last_service_date, current_date):
        self.__last_service_date = last_service_date
        self.__current_date = current_date
    
    # Implementing needs_service() method from Battery interface
    def needs_service(self):
        service_threshold_date = self.__last_service_date.replace(year=self.__last_service_date.year + 3)
        return service_threshold_date < self.__current_date
      

