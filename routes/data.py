from flask import Blueprint, request, jsonify

from db import get_db_connexion, close_db_connexion

import db.airports, db.flights, db.airlines

from utils import token_required

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
    conn = get_db_connexion()
    cursor = conn.cursor()

    all_flights = db.flights.get_flights(cursor)
    if all_flights == None:
        conn.rollback()
        close_db_connexion(cursor, conn)
        return "Error: while fetching flights", 500
    conn.commit()
    close_db_connexion(cursor, conn)
    return jsonify({"flights": [dict(flight) for flight in all_flights]})


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
    conn = get_db_connexion()
    cursor = conn.cursor()

    all_airports = db.airports.get_airports(cursor)
    if all_airports == None:
        conn.rollback()
        close_db_connexion(cursor, conn)
        return "Error: while fetching airports", 500
    conn.commit()
    close_db_connexion(cursor, conn)
    return jsonify({"airports": [dict(airport) for airport in all_airports]})


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
    conn = get_db_connexion()
    cursor = conn.cursor()

    all_airlines = db.airlines.get_airlines(cursor)
    if all_airlines == None:
        conn.rollback()
        close_db_connexion(cursor, conn)
        return "Error: while fetching airlines", 500
    conn.commit()
    close_db_connexion(cursor, conn)
    return jsonify({"airlines": [dict(airline) for airline in all_airlines]})
