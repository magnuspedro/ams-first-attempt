from flask import Blueprint, jsonify, request
from ams.models import Ticket
from ams.tickets import schema
from ams.config import db
tickets = Blueprint('tickets', __name__)


@tickets.route("/ticket")
def get_ticket():

    obj_ticket = db.session.query(ticket).all()

    schema = schema.TicketSchema(many=True)
    tickets = schema.dump(obj_ticket)

    return jsonify(tickets.data)


@tickets.route("/ticket", methods=['POST'])
def register_ticket():
    posted_ticket = schema.TicketSchema().load(request.get_json())

    ticket = Ticket(**posted_ticket.data)

    db.session.add(ticket)
    db.session.commit()

    new_ticket = schema.TicketSchema().dump(ticket).data

    return jsonify(new_ticket), 201
