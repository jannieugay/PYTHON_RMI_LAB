from Pyro5.api import expose
from Product import Product

@expose
class ProductImpl(Product):

    # Attributes of product
    def __init__(self, newName, newDescription, newPrice):
        self.name = newName
        self.description = newDescription
        self.price = newPrice

    def getName(self) -> str:
        return self.name

    def getDescription(self) -> str:
        return self.description

    def getPrice(self) -> float:
        return self.price

    def changeProductName(self, newName: str) -> None:
        self.name = newName