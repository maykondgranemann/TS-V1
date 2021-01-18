class Seller:

    def __init__(self, name: str, telephone: str, email: str, id: int = None) -> None:
        self.__name = name
        self.__telephone = telephone
        self.__email = email
        self.__id = id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def telephone(self):
        return self.__telephone
    
    @property
    def email(self):
        return self.__email
    
    @property
    def id(self):
        return self.__id
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @telephone.setter
    def telephone(self, telephone):
        self.__telephone = telephone
    
    @email.setter
    def email(self, email):
        self.__email = email
    
    @id.setter
    def id(self, id):
        self.__id = id