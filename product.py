class Product:
    """Represents and manages a single product."""

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    # Read-only access to attributes
    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock

    def update_stock(self, quantity):
        """Set stock to a new quantity. Product controls what is valid."""
        if not isinstance(quantity, int):
            raise ValueError("Stock must be a whole number.")
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")
        self.__stock = quantity

    def display_information(self, detailed=False):
        if detailed:
            print("-" * 35)
            print(f"ID: {self.__product_id}")
            print(f"Name: {self.__name}")
            print(f"Price: ${self.__price:.2f}")
            print(f"Stock: {self.__stock}")
            print("-" * 35)
        else:
            print(
                f"ID: {self.__product_id} | Name: {self.__name} | "
                f"Price: ${self.__price:.2f} | Stock: {self.__stock}"
            )

    # Convert to/from a dictionary so the JSON file keeps the Week 5 format
    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"], data["price"], data["stock"])