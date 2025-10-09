from sqlite3 import Cursor


def get_airport_id_by_icao(cursor: Cursor, icao: str) -> int | None:
    # TODO
    pass


def get_all_airport_info_by_id(cursor: Cursor, id: int) -> dict | None:
    # TODO
    pass


def get_airports(cursor):
    """Get all airports from the database.

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
        query = "SELECT * FROM Airports"
        cursor.execute(query, [])

    except sqlite3.IntegrityError as error:
        print(
            f"An integrity error occurred while fetching the airports: {error}")
        return None
    except sqlite3.Error as error:
        print(f"A database error occurred while fetching the airports: {error}")
        return None

    return cursor.fetchall()