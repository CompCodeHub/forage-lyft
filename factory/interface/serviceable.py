from abc import ABC, abstractmethod

# Serviceable interface
class Serviceable(ABC):

    # Abstract needs_service method
    @abstractmethod
    def needs_service():
        pass