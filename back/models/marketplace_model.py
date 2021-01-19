from sqlalchemy import Column, String, Integer
from back.models.base_model import BaseModel


class Marketplace(BaseModel):
    __tablename__ = 'marketplace'

    name = Column(String)
    description = Column(String)

    def __init__(self, name:str, description:str) -> None:
        self.name = name
        self.description = description

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}"