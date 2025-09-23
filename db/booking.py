from sqlite3 import Cursor


def create_booking(cursor: Cursor, user_name: str, flight_id: int) -> bool:
    # TODO
    pass


def get_usernames_by_flight(cursor: Cursor, flight_id: int) -> list[str] | None:
    # TODO
    pass


def get_bookings_by_user(cursor: Cursor, user_name: str) -> list[dict] | None:
    # TODO
    pass


def delete_booking(cursor: Cursor, user_name: str, flight_id: int) -> bool:
    # TODO
    pass
