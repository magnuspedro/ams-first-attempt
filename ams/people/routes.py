from flask import Blueprint, jsonify, request
from ams.models import Person
from ams.people import schema
from ams.config import db

people = Blueprint('people', __name__)

# Person Register


@people.route("/person")
def get_person():

    obj_person = db.session.query(Person).all()

    schema = schema.PersonSchema(many=True)
    persons = schema.dump(obj_person)

    return jsonify(persons.data)


@people.route("/person", methods=['POST'])
def register_person():
    posted_person = schema.PersonSchema().load(request.get_json(), session=db.session)

    person = posted_person.data

    db.session.add(person)
    db.session.commit()

    new_person = schema.PersonSchema().dump(person).data

    return jsonify(new_person), 201
