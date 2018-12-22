from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_marshmallow import Marshmallow


app = Flask(__name__, template_folder="static/public")

app.config['SECRET_KEY'] = 'c8d3c67debd089733789'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/ams'
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
