from flask import Blueprint, jsonify

from utils import token_required

orders_bp = Blueprint("orders", __name__)


@orders_bp.route("/<int:book_id>")
def get_booking(order_id: int):
    """Get an booking in the database based on its booking id.

    Parameters
    ----------
    order_id
        id of the booking to get

    Returns
    -------
    data
        all data about the booking if correctly fetched
        a message "Booking does not exist" if the booking is not found in
            the database.
        an error message "Error: while fetching the booking" if an error
            occured while fetching the booking.
    status_code
        200 if the booking is correctly fetched
        404 if the booking does not exist in the database
        500 if an error occured while fetching the booking
    """
    # TODO
    return jsonify({"message": "TODO"})


@orders_bp.route("/", methods=["POST"])
@token_required
def create_booking():
    """Create a new booking.
    The username and flight id must be passed in the JSON body of the POST request.

    Parameters
    ----------
    user_name
        username of the user (as defined in the database)
    flight_id
        id of the flight the user wants to book

    Returns
    -------
    data
        a message "Booking created" if successfully inserted
        a message "Failed to create booking" if the booking could not be inserted
        an error message "Error: <details>" if an error occurred while inserting
    status_code
        201 if the booking is correctly created
        400 if the booking could not be created
        500 if an error occurred while creating the booking
    """
    return jsonify({"message": "TODO"})


@orders_bp.route("/user/<string:user_name>", methods=["GET"])
@token_required
def get_user_bookings(user_name):
    """Get all bookings of a user.

    Parameters
    ----------
    user_name
        username of the user (as defined in the database)

    Returns
    -------
    data
        list of bookings if the user has bookings
        a message "No bookings found" if the user has no bookings
        an error message "Error: <details>" if an error occurred while fetching
    status_code
        200 if the bookings are correctly fetched
        404 if no bookings are found
        500 if an error occurred while fetching
    """
    # TODO
    return jsonify({"message": "TODO"})


@orders_bp.route("/flight/<int:flight_id>", methods=["GET"])
@token_required
def get_flight_users(flight_id):
    """Get all usernames booked on a flight.

    Parameters
    ----------
    flight_id
        id of the flight (as defined in the database)

    Returns
    -------
    data
        list of usernames if found
        a message "No users found" if the flight has no bookings
        an error message "Error: <details>" if an error occurred while fetching
    status_code
        200 if the users are correctly fetched
        404 if no users are found
        500 if an error occurred while fetching
    """
    # TODO
    return jsonify({"message": "TODO"})
