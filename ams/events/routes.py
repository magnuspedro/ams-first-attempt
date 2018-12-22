from flask import Blueprint, jsonify, request
from ams.models import Event
from ams.events import schema
from ams.config import db
events = Blueprint('events', __name__)


@events.route("/event")
def get_event():

    obj_event = db.session.query(Event).all()

    schema = schema.EventSchema(many=True)
    events = schema.dump(obj_event)

    return jsonify(events.data)


@events.route("/event", methods=['POST'])
def register_event():
    posted_event = schema.EventSchema().load(request.get_json(), session=db.session)

    event = posted_event.data

    db.session.add(event)
    db.session.commit()

    new_event = schema.EventSchema().dump(event).data

    return jsonify(new_event), 201
