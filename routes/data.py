from flask import Blueprint, request, jsonify

data_bp = Blueprint("data", __name__)


@data_bp.route("/flights")
def get_all_flights():
    """Get all flights in the database.

    Returns
    -------
    data
        all flights in the database
        an error message "Error: while fetching flights" if an error occured
            while fetching the flights.
    status_code
        200 if the flights are correctly fetched
        500 if an error occured while fetching the flights
    """
    # TODO
    return jsonify({"message": "TODO"})


@data_bp.route("/airports")
def get_all_airports():
    """Get all airports in the database.

    Returns
    -------
    data
        all airports in the database
        an error message "Error: while fetching airports" if an error occured
            while fetching the airports.
    status_code
        200 if the airports are correctly fetched
        500 if an error occured while fetching the airports
    """
    # TODO
    return jsonify({"message": "TODO"})


@data_bp.route("/airlines")
def get_all_airlines():
    """Get all airlines in the database.

    Returns
    -------
    data
        all airlines in the database
        an error message "Error: while fetching airlines" if an error occured
            while fetching the airlines.
    status_code
        200 if the airlines are correctly fetched
        500 if an error occured while fetching the airlines
    """
    # TODO
    return jsonify({"message": "TODO"})
