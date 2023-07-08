from battery.battery import Battery

# Nubbin Battery class implements Battery interface
class NubbinBattery(Battery):

    # Constructor
    def __init__(self, last_service_date, current_date):
        self.__last_service_date = last_service_date
        self.__current_date = current_date
    
    # Implementing needs_service() method from Battery interface
    def needs_service(self):
        service_threshold_date = self.__last_service_date.replace(year=self.__last_service_date.year + 4)
        return service_threshold_date < self.__current_date
    