from flask import Flask, request, jsonify

from typing import Iterable

from models import Product, ProductSchema 
from controllers import product_controller
from base import engine, Base

app = Flask(__name__)


def serialize(products):
    ps = ProductSchema()
    return list(map(lambda prod: ps.dump(prod), products))


@app.route("/products", methods=['GET', 'POST'])
def get_products():
    
    if request.method == "POST":
        name = request.json.get("name")
        desc = request.json.get("desc")
        value = float(request.json.get("value"))

        return jsonify(
            {"product": serialize([product_controller.insert(name, desc, value)])}
        )

    return jsonify(
        {"products": serialize(list(product_controller.get()))}
    )

@app.route("/products/<int:id>", methods=['PUT'])
def change_user(id: int):
    try:
        name = request.json.get("name")
        desc = request.json.get("desc")
        value = request.json.get("value")
        return jsonify(
            {"product": serialize([product_controller.change(id, name=name, desc=desc, value=value)])}
        )
    except KeyError:
        pass

@app.route("/delete_product/<int:id>", methods=['DELETE'])
def delete_user(id: int):
    return jsonify(
        {"product_deleted": serialize([product_controller.delete(id)])}
    )


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run()