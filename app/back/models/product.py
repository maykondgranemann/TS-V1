class Product:

    def __init__(self, name: str, description: str, price: float, id: int = None):
        self.name = name
        self.description = description
        self.price = price
        self.id = id
    
    @property
    def id(self):
        return self.id
    
    @property
    def name(self):
        return self.name

    @property
    def description(self):
        return self.description

    @property
    def price(self):
        return self.price

    @name.setter
    def name(self, name):
        self.name = name
    
    @description.setter
    def description(self, description):
        self.description = description
   
    @price.setter
    def price(self, price):
        self.price = price
