from abc import ABC, abstractmethod

class Product(ABC):

    # Lets us define API
    @abstractmethod
    def getName(self) -> str:
        pass

    @abstractmethod
    def getDescription(self) -> str:
        pass

    @abstractmethod
    def getPrice(self) -> float:
        pass

    @abstractmethod
    def changeProductName(self, newName: str) -> None:
        pass