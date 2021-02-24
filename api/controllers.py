from sqlalchemy.orm import Session

from models import Product
from base import Session as sess


class InvalidProductAttribute(Exception):
    pass


class ProductController():
    """
    Controller class for Product model, all database persistence
    questions related are handled in ProducController class.

    Products can be inserted, retrieved, altered and deleted
    """

    _PRODUCTS_ITEMS = [
        'name',
        'desc',
        'value' 
    ]
    
    def __init__(self, session: Session):
        self.session = session

    def insert(self, name: str, desc: str, value: float) -> Product:
        p = Product(name, desc, value)
        self.session.add(p)
        self.session.commit()
        return p

    def change(self, id: int, *args, **kwargs) -> Product:
        product = self.session.query(Product).filter_by(id=id).first()
        for k in kwargs:
            v = kwargs[k]
            if not k in self._PRODUCTS_ITEMS:
                raise InvalidProductAttribute(f'Product model does not has {k} attr')
            if k == "name" and v is not None:
                product.name = v
            elif k == "desc" and v is not None:
                product.desc = v
            elif k == "value" and v is not None:
                product.value = float(v)
        
        self.session.commit()
        return product

    def delete(self, id: int) -> Product:
        product = self.session.query(Product).filter_by(id=id)
        p = product.first()
        product.delete()
        self.session.commit()
        return p

    def get(self):
        return self.session.query(Product).all()

    def get_id(self, name: str):
        return self.session.query(Product).filter_by(name=name).first().id


product_controller = ProductController(sess())