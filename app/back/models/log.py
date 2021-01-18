class Log:

    def __init__(self, date: str, message: str, id: int = None):
        self.__date = date
        self.__message = message
        self.__id = id

    @property
    def date(self):
        return self.__date
    
    @property
    def message(self):
        return self.__message
    
    @property
    def id(self):
        return self.__id

    @date.setter
    def date(self, date):
        self.__date = date
    
    @message.setter
    def message(self, message):
        self.__message = message
    
    @id.setter
    def id(self, id):
        self.__id = id