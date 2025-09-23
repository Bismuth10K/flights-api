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

