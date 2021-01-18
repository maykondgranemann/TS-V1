class Category:

    def __init__(self, name: str, description: str, id: int = None) -> None:
        self.__id = id
        self.__name = name
        self.__description = description
    
    @property
    def name(self):
        return self.__name
    
    @property
    def description(self):
        return self.__description
    
    @property
    def id(self):
        return self.__id
    
    @name.setter
    def name(self, name)
        self.__name = name
    
    @description.setter
    def description(self, description)
        self.__description = description
    
    @id.setter
    def id(self, id)
        self.__id = id
