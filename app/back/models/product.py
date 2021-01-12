class Product:

    def __init__(self, name: str, description: str, price: float, id: int = None):
        self.name = name
        self.description = description
        self.price = price
        self.id = id