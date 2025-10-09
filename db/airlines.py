from sqlite3 import Cursor


def get_airlines_by_country(cursor: Cursor, iso_code: str) -> list[dict] | None:
    # TODO
    pass


def get_airline_by_id(cursor: Cursor, id: str) -> dict | None:
    # TODO
    pass


def remove_airline_by_id(cursor: Cursor, id: str) -> bool:
    # TODO
    pass


def get_airlines(cursor):
    """Get all airlines from the database.

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
        query = "SELECT * FROM Airlines"
        cursor.execute(query, [])

    except sqlite3.IntegrityError as error:
        print(
            f"An integrity error occurred while fetching the airlines: {error}")
        return None
    except sqlite3.Error as error:
        print(f"A database error occurred while fetching the airlines: {error}")
        return None

    return cursor.fetchall()