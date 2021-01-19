class Seller:
    def __init__(self, name: str, phone: str, email: str, id: int = None) -> None:
        self.__id = id
        self.__name = name
        self.__phone = phone
        self.__email = email

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id) -> None:
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        self.__name = name

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone) -> None:
        self.__phone = phone

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email) -> None:
        self.__email = email

    def __str__(self):
        return f'Seller Name: {self.__name} - Seller id: {self.__id}'


s = Seller('Jeff', '4199955533', 'jeff@mail.com', 1)

print(s)
print(s.name, s.email, s.phone, s.id)

s.phone = '4166666666'
s.name = 'Mudrei'

print(s)
print(s.name, s.email, s.phone, s.id)
