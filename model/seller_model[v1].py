class Seller:
    # def __init__(self, name: str, phone: str, email: str, id: int = None) -> None:
    #     self.__id = id
    #     self.__name = name
    #     self.__phone = phone
    #     self.__email = email

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = id

    @property
    def name(self) -> None:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def phone(self):
        return self.__phone

    @phone.setter()
    def phone(self, phone: str) -> None:
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        self.__email = email
