from flask import Blueprint, jsonify, request
from ams.models import Product
from ams.products import schema
from ams.config import db
products = Blueprint('products', __name__)


@products.route("/product")
def get_product():

    obj_product = db.session.query(Product).all()

    schema = schema.ProductSchema(many=True)
    products = schema.dump(obj_product)

    return jsonify(products.data)


@products.route("/product", methods=['POST'])
def register_product():
    posted_product = schema.ProductSchema().load(request.get_json(), session=db.session)

    product = posted_product.data

    db.session.add(product)
    db.session.commit()

    new_product = schema.ProductSchema().dump(product).data

    return jsonify(new_product), 201
