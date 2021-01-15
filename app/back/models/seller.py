class Seller:

    def __init__(self, name: str, telephone: str, email: str, id: int = None) -> None:
        self.name = name
        self.telephone = telephone
        self.email = email
        self.id = id