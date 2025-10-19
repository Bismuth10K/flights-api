from flask import Flask

from db import init_database
import db.countries

from routes.auth import auth_bp
from routes.bookings import orders_bp
from routes.data import data_bp
from routes.flights import flights_bp
from routes.users import users_bp

from test_users import *

def create_app():
    """Create a Flask application and add blueprints with all routes.

    Returns
    -------
    app
        the application created
    """
    # Create the default app
    app = Flask(__name__)

    # Add a first blueprints with all routes for the API
    # Take a look at the file ./routes/users.py to have more
    # details about the routes you have access to.
    app.register_blueprint(auth_bp, url_prefix="/login")
    app.register_blueprint(data_bp, url_prefix="/data")
    app.register_blueprint(flights_bp, url_prefix="/flights")
    app.register_blueprint(orders_bp, url_prefix="/orders")
    app.register_blueprint(users_bp, url_prefix="/users")

    return app


# Entry point of the application
if __name__ == "__main__":
    app = create_app()
    init_database()
    test_insert_user()
    test_update_password_existing_user()
    print_users()
    app.run(port=5000, debug=False)
