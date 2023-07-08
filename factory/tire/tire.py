from abc import ABC, abstractmethod

# Tire Interface
class Tire(ABC):

    # Abstract needs_service() method
    @abstractmethod
    def needs_service():
        pass