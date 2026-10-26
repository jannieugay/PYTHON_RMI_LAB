
from abc import ABC, abstractmethod

import Pyro5.api


class Product(ABC):
    """Remote interface: what a client can do with a Product."""

    @abstractmethod
    def get_name(self) -> str: ...

    @abstractmethod
    def get_price(self) -> float: ...

    @abstractmethod
    def get_description(self) -> str: ...


class ProductService(ABC):
    """Remote interface of the server object (ServerImpl in the Java version)."""

    @abstractmethod
    def list_products(self) -> list: ...

    @abstractmethod
    def get_product(self, name: str): ...

    @abstractmethod
    def add_product(self, name: str, price: float, description: str) -> str: ...


# Name and address the server is published under (like the RMI registry entry)
SERVER_OBJECT_ID = "product.server"
SERVER_HOST = "localhost"
SERVER_PORT = 9080
SERVER_URI = f"PYRO:{SERVER_OBJECT_ID}@{SERVER_HOST}:{SERVER_PORT}"

# Pyro5 re-exports for convenience
expose = Pyro5.api.expose
