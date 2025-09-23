from sqlite3 import Cursor


def get_all_countries(cursor: Cursor) -> list[dict]:
    # TODO
    pass


def get_all_countries_sorted_by_name(cursor: Cursor, ascending: bool) -> list[dict]:
    # TODO
    pass


def get_country_name_by_code(cursor: Cursor, iso_code: str) -> str | None:
    # TODO
    pass
