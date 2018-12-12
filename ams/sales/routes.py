from flask import Blueprint, jsonify, request
from ams.models import Sales
from ams.sales import schema
from ams.config import db
sales = Blueprint('sales', __name__)


@sales.route("/sale")
def get_sales():

    obj_sales = db.session.query(sale).all()

    schema = schema.SalesSchema(many=True)
    sales = schema.dump(obj_sales)

    return jsonify(sales.data)


@sales.route("/sale", methods=['POST'])
def register_sales():
    posted_sales = schema.SalesSchema().load(request.get_json())

    sale = Sales(**posted_sales.data)

    db.session.add(sale)
    db.session.commit()

    new_sales = schema.SalesSchema().dump(sale).data

    return jsonify(new_sales), 201
