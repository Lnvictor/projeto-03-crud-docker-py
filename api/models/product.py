"""
Product Model abstraction
"""
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy import Column, Integer, String, Float
from base import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(String)
    value = Column(Float)

    def __init__(self, name: str, desc: str, value: float):
        self.name = name
        self.desc = desc
        self.value = value

    def __repr__(self):
        return self.name


class ProductSchema(SQLAlchemySchema):
    """
    Marshmallow schema serializer
    """
    class Meta:
        model = Product

    id = auto_field()
    name = auto_field()
    desc = auto_field()
    value = auto_field()