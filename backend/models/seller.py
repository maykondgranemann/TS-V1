from backend.models.base_model import BaseModel
import sqlalchemy as db


class Seller(BaseModel):
    __tablename__ = 'seller'
    name = db.Column(db.String(length=50))
    phone = db.Column(db.String(length=50))
    mail = db.Column(db.String(length=50))

    def __init__(self, name: str, phone: str, mail: str):
        self.set_name(name)
        self.set_phone(phone)
        self.set_mail(mail)

    def set_name(self, name_parm: str) -> None:
        if isinstance(name_parm, str):
            self.name = name_parm
        else:
            raise ValueError("The name must be a String")
    def set_phone(self, phone_parm: str) -> None:
        if isinstance(phone_parm, str):
            self.phone = phone_parm
        else:
            raise ValueError("The phone must be a String")
        
    def set_mail(self, mail_parm: str) -> None:
        if isinstance(mail_parm, str):
            self.mail = mail_parm
        else:
            raise ValueError("The mail must be a String")
