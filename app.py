from flask import Flask

from db import init_database

from routes.users import users_bp
from routes.data import data_bp

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
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(data_bp, url_prefix="/data")

    # TODO - ADD OTHER BLUEPRINTS

    return app


# Entry point of the application
if __name__ == "__main__":
    app = create_app()
    init_database()
    test_insert_user()
    print_users()
    app.run(port=5000, debug=False)
