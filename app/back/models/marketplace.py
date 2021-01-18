class Marketplace:

    def __init__(self, name: str, description: str, id: int = None) -> None:
        self.name = name
        self.description = description
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
    
    @name.setter
    def name(self, name):
        self.name = name
    
    @description.setter
    def description(self, description):
        self.description = description