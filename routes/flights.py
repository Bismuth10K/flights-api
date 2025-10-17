from flask import Blueprint, jsonify, request

from utils import token_required

flights_bp = Blueprint("flights", __name__)


@flights_bp.route("/", methods=["POST"])
@token_required
def create_flight():
    """Insert a new flight.
    The flight details must be passed in the JSON body of the POST request.

    Parameters
    ----------
    departure_time
        departure time
    arrival_time
        arrival time
    price
        price of the flight
    src_icao
        ICAO code of the source airport
    dest_icao
        ICAO code of the destination airport
    plane_icao
        ICAO code of the plane used
    airline_icao
        ICAO code of the airline operating the flight
    Returns
    -------
    data
        a message "Flight created" if successfully inserted
        a message "Failed to create flight" if the flight could not be inserted
        an error message "Error: <details>" if an error occurred while inserting
    status_code
        201 if the flight is correctly created
        400 if the flight could not be created
        500 if an error occurred while creating the flight
    """
    # TODO
    return jsonify({"message": "TODO"})



@flights_bp.route("/<int:flight_id>", methods=["GET"])
def get_flight(flight_id):
    """Get a flight by its ID.

    Parameters
    ----------
    flight_id
        id of the flight (as defined in the database)

    Returns
    -------
    data
        flight data as JSON if found
        a message "Flight not found" if the flight does not exist
        an error message "Error: <details>" if an error occurred while fetching
    status_code
        200 if the flight is correctly fetched
        404 if the flight does not exist
        500 if an error occurred while fetching
    """
    # TODO
    return jsonify({"message": "TODO"})

@flights_bp.route("/search", methods=["GET"])
def search_flights():
    """Get all flights between two cities.
    The source and destination cities must be passed as query parameters.

    Parameters
    ----------
    src_city
        name of the source city (as defined in the database)
    dest_city
        name of the destination city (as defined in the database)

    Returns
    -------
    data
        list of flights if found
        a message "No flights found" if there are no results
        an error message "Error: <details>" if an error occurred while fetching
    status_code
        200 if the flights are correctly fetched
        404 if no flights are found
        500 if an error occurred while fetching
    """
    # TODO
    return jsonify({"message": "TODO"})