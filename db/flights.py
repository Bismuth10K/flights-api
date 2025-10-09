import sqlite3
from sqlite3 import Cursor

import utils


def insert_flight(
    cursor: Cursor,
    departure: str,
    arrival: str,
    price: float,
    src_icao: str,
    dest_icao: str,
    plane_icao: str,
    airline_icao: str,
) -> bool:
    # TODO
    pass


def get_flight_by_id(cursor: Cursor, flight_id: int) -> dict | None:
    # TODO
    pass


def remove_flight_by_id(cursor: Cursor, flight_id: int) -> bool:
    # TODO
    pass


def get_flights_by_src_city_and_dest_city(
    cursor: Cursor, src_city: str, dest_city: str
) -> list[dict] | None:
    # TODO
    pass


def get_flights(cursor):
    """Get all flights from the database.

    Parameters
    ----------
    cursor:
        The object used to query the database.

    Returns
    -------
    list
        The list of all the user information if no error occurs, None otherwise.
    """
    try:
        query = "SELECT * FROM Flights"
        cursor.execute(query, [])

    except sqlite3.IntegrityError as error:
        print(
            f"An integrity error occurred while fetching the flights: {error}")
        return None
    except sqlite3.Error as error:
        print(f"A database error occurred while fetching the flights: {error}")
        return None

    return cursor.fetchall()