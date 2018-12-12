from ams.tickets.routes import tickets
from ams.sales.routes import sales
from ams.modalities.routes import modalities
from ams.main.routes import main
from ams.products.routes import products
from ams.events.routes import events
from ams.people.routes import people
from ams.config import app

app.register_blueprint(people)
app.register_blueprint(events)
app.register_blueprint(products)
app.register_blueprint(main)
app.register_blueprint(modalities)
app.register_blueprint(sales)
app.register_blueprint(tickets)
