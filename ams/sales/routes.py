from flask import Blueprint, jsonify, request
from ams.models import Sales, Sell
from ams.sales import schema
from ams.config import db
sales = Blueprint('sales', __name__)


@sales.route("/sales")
def get_sales():

    obj_sales = db.session.query(sale).all()

    schema = schema.SalesSchema(many=True)
    sales = schema.dump(obj_sales)

    return jsonify(sales.data)


@sales.route("/sales", methods=['POST'])
def register_sales():
    posted_sales = schema.SalesSchema().load(request.get_json(), session=db.session)

    sale = posted_sales.data
    # Calculate the value of the product, I may have to delete it whe the ux get ready
    value = 0.0
    for product in sale.transaction:
        prices = Sell.query.filter_by(id=product.sell_id).all()
        for price in prices:
            value += price.price
    value = (value - (value * (sale.discount / 100)))
    sale.value = (value + (value * (sale.taxes.percentage / 100)))
    db.session.add(sale)
    db.session.commit()

    new_sales = schema.SalesSchema().dump(sale).data

    return jsonify(new_sales), 201
