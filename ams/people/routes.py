from flask import Blueprint, jsonify, request
from ams.models import Person
from ams.people.schema import PersonSchema
from ams.student.schema import StudentSchema
from ams.config import db
import sqlalchemy


people = Blueprint('people', __name__)


@people.route("/person")
def get_person():
    person = Person()

    obj_person = person.query.all()

    schemaPerson = PersonSchema(many=True)
    persons = schemaPerson.dump(obj_person)

    return jsonify(persons.data)


@people.route("/person", methods=['POST'])
def register_person():

    posted_person = StudentSchema().load(request.get_json(), session=db.session)

    person = posted_person.data

    try:
        db.session.add(person)
        db.session.commit()
        new_person = StudentSchema().dump(person).data
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        return "User Already Exists", 404

    return jsonify(new_person), 201
