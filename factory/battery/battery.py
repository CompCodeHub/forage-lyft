from abc import ABC, abstractmethod

# Battery Interface
class Battery(ABC):

    # Abstract needs_service() method
    @abstractmethod
    def needs_service():
        pass