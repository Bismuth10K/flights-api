from sqlite3 import Cursor


def insert_city(cursor: Cursor, city_name: str, iso_country: str) -> bool:
    # TODO
    pass


def get_city_id_by_name_and_country_code(
    cursor: Cursor, name: str, iso_code: str
) -> int | None:
    # TODO
    pass


def get_city_name_by_id(cursor: Cursor, id: str) -> str | None:
    # TODO
    pass


def update_city_name(cursor: Cursor, id: str, new_name: str) -> bool:
    # TODO
    pass
