from sqlite3 import Cursor


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
