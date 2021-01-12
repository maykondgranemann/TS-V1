class Seller:

    def __init__(self, name: str, phone: str, mail: str, id: int = None) -> None:
        self.name = name
        self.phone = phone
        self.mail = mail
        self.id = id