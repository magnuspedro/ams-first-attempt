from datetime import datetime
from ams.config import db
from flask_login import UserMixin


def load_person(person_id):
    return Person.gery.get(int(person_id))


class Person(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    cpf = db.Column(db.String(15), unique=True, nullable=False)
    rg = db.Column(db.String(15), nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    course = db.Column(db.String(10), nullable=False)
    partner = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(45), nullable=False)
    birth = db.Column(db.Date, nullable=False)
    password = db.Column(db.String(200), nullable=True)
    post = db.Column(db.String(100), nullable=True)
    salesperson = db.relationship('Salesperson', uselist=False, backref=db.backref('person_salesperson'), lazy='joined')
    student = db.relationship('Student', uselist=False, backref=db.backref('person_student'), lazy='joined')

    # def __repr__(self):
    # return f"{self.id} {self.name} {self.cpf}"


class Salesperson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id', ondelete='CASCADE'), nullable=False)
    sales = db.relationship('Sales', backref=db.backref('salesperson_sales'), lazy='joined')
    distributions = db.relationship('Distributions', backref=db.backref('sales_distributions'), lazy='dynamic')


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id', ondelete='CASCADE'), nullable=False)
    sales = db.relationship('Sales', backref=db.backref('student_sales'), lazy='joined')
    team = db.relationship('Team', backref=db.backref('student_team'), lazy='dynamic')


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(280), nullable=True)
    amount = db.Column(db.Float, nullable=False)
    size = db.Column(db.String(15), nullable=False)
    color = db.Column(db.String(15), nullable=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id', ondelete='CASCADE'), nullable=False)
    bought = db.relationship('Bought', uselist=False, backref=db.backref('product_bought'), lazy='joined')
    sell = db.relationship('Sell', uselist=False, backref=db.backref('product_sell'), lazy='joined')


class Bought(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id', ondelete='CASCADE'), nullable=False)
    price = db.Column(db.Float, nullable=False)


class Sell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id', ondelete='CASCADE'), nullable=False)


class Transaction(db.Model):
    amount = db.Column(db.Float, nullable=False)
    sell_id = db.Column(db.Integer, db.ForeignKey('sell.id', ondelete='CASCADE'), primary_key=True)
    sales_id = db.Column(db.Integer, db.ForeignKey('sales.id', ondelete='CASCADE'), primary_key=True)
    sell = db.relationship('Sell', backref=db.backref('transaction_sell'), lazy='joined')


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    starting_date = db.Column(db.Date, nullable=False)
    ending_date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Float, nullable=False)
    product = db.relationship('Product', backref=db.backref('event_product'), lazy='dynamic')
    competition = db.relationship('Modality', secondary='competition', backref=db.backref('event_competition'), lazy='dynamic')
    ticket = db.relationship('Ticket', backref=db.backref('ticket'), lazy='joined')

    # def __repr__(self):
    # return f"{self.id},{self.name}"


class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'), nullable=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id', ondelete='CASCADE'), nullable=True)
    salesperson_id = db.Column(db.Integer, db.ForeignKey('salesperson.id', ondelete='CASCADE'), nullable=False)
    transaction = db.relationship('Transaction', backref=db.backref('sales_transaction'), lazy='dynamic')
    taxes = db.relationship('Taxes', backref=db.backref('sales_taxes'), lazy='joined')
    shipping = db.relationship('Shipping', backref=db.backref('sales_shipping'), lazy='dynamic')

    # def __repr__(self):
    # return f"Sales('{self.value}, {self.discount}, {self.taxes},
    # {self.description}, {self.date}')"


class Taxes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    percentage = db.Column(db.Float, default=0.0, nullable=False)
    sales_id = db.Column(db.Integer, db.ForeignKey('sales.id', ondelete='CASCADE'), nullable=False)


class Modality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    fee = db.Column(db.Float, default=0.0, nullable=False)
    sex = db.Column(db.String(1), nullable=False)


class Team(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey(
        'student.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    modality_id = db.Column(db.Integer, db.ForeignKey(
        'modality.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    modality = db.relationship('Modality', backref=db.backref('team_modality'), lazy='joined')


competition = db.Table('competition',
                       db.Column('event_id', db.Integer,
                                 db.ForeignKey('event.id', ondelete='CASCADE')),
                       db.Column('modality_id', db.Integer,
                                 db.ForeignKey('modality.id', ondelete='CASCADE')))

# Until here alles gut but ticket still giving me headche


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100), nullable=True)
    staus = db.Column(db.Integer, default=0, nullable=True)
    amount = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    lot = db.Column(db.String(20), nullable=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id', ondelete='CASCADE'), nullable=False)
    distributions = db.relationship('Distributions', backref=db.backref('ticket_distributions'), lazy='dynamic')
    sales = db.relationship('Sales', backref=db.backref('ticket_sales'), lazy='joined')


class Shipping(db.Model):
    amount = db.Column(db.Integer, nullable=False)
    sales_id = db.Column(db.Integer, db.ForeignKey('sales.id', ondelete='CASCADE'), primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id', ondelete='CASCADE'), primary_key=True)

    ticket = db.relationship('Ticket', backref=db.backref('shipping_ticket'), lazy='joined')


class Distributions(db.Model):
    amount_given = db.Column(db.Integer, nullable=False)
    amount_sold = db.Column(db.Integer, nullable=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id', ondelete='CASCADE'), primary_key=True)
    salesperson_id = db.Column(db.Integer, db.ForeignKey('salesperson.id', ondelete='CASCADE'), primary_key=True)
