from flask import Flask

from db import init_database
import db.countries

from routes.users import users_bp

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

    # TODO - ADD OTHER BLUEPRINTS

    return app


# Entry point of the application
if __name__ == "__main__":
    app = create_app()
    init_database()
    app.run(port=5000, debug=False)
