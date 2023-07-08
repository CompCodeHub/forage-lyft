from abc import ABC, abstractmethod

# Engine Interface
class Engine(ABC):

    # Abstract needs_service() method
    @abstractmethod
    def needs_service():
        pass