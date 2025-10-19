import sqlite3
from sqlite3 import Cursor

import utils


def insert_user(user, cursor):
    """Inserts an user into to the database.

    Parameters
    ----------
    user: a dictionnary
        User personal data: user["username"] and user["password"].
    cursor:
        The object used to query the database.

    Returns
    -------
    bool
        True if no error occurs, False otherwise.
    """
    try:
        # The user is described by two attributes: username and password.
        # The values of these attributes are available in the dictionary user, one of the parameters of this function.
        # So, we need to write our insert query in such a way that the values are obtained from the dictionary user.
        # Our insert query contains two question marks (?) that indicate that the values will be specified later.
        #
        #  IMPORTANT:
        #
        # * The query assumes that you called User the table with the user personal data. If you gave it another name, CHANGE the query accordingly.
        #
        # * The query assumes that in your table User the columns are defined in this order:
        # username, password.
        # IF THE ORDER in which you created the columns IS DIFFERENT, CHANGE this variable accordingly.

        query_insert_user = "INSERT INTO User (username, password) VALUES (?, ?)"
        cursor.execute(query_insert_user,
                       (user["username"], utils.hash_password(user["password"])))

    except sqlite3.IntegrityError as error:
        print(f"An integrity error occurred while insert the user: {error}")
        return False
    except sqlite3.Error as error:
        print(f"A database error occurred while inserting the user: {error}")
        return False

    return True


def get_user(username, cursor):
    """Get an user from the database based on its username and a list of
    the orders assigned to the user.

    Parameters
    ----------
    username: string
        User username.
    cursor:
        The object used to query the database.

    Returns
    -------
    dict
        The user username, password and orders if no error occurs, None otherwise.
    """
    try:
        query_get_user = "SELECT * FROM User WHERE username = ?"
        cursor.execute(query_get_user, [username])

        user = cursor.fetchone()

        # query_get_orders = "SELECT id FROM Order WHERE user_username = ?"
        # cursor.execute(query_get_orders, [username])

        # orders = cursor.fetchall()

    except sqlite3.IntegrityError as error:
        print(f"An integrity error occurred while fetching the user: {error}")
        return None
    except sqlite3.Error as error:
        print(f"A database error occurred while fetching the user: {error}")
        return None

    return {
        "username": user["username"],
        # "orders": orders,
        "password": user["password"],
    }


def get_users(cursor):
    """Get all users from the database.

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
        query_get_users = "SELECT username FROM User"
        cursor.execute(query_get_users, [])

    except sqlite3.IntegrityError as error:
        print(
            f"An integrity error occurred while fetching the users: {error}")
        return None
    except sqlite3.Error as error:
        print(f"A database error occurred while fetching the users: {error}")
        return None

    return cursor.fetchall()


def update_password(username, password, cursor):
    """Update the password of an user.

    Parameters
    ----------
    username: string
        User username.
    password: bytes
        New password
    cursor:
        The object used to query the database.

    Returns
    -------
    bool
        True if no error occurs, False otherwise.
    """
    try:
        val = utils.hash_password(password)
        cursor.execute(f"UPDATE User SET password = {val} WHERE username = {username}")
        return True
    except sqlite3.IntegrityError as error:
        print(f"An integrity error occurred while fetching the users: {error}")
        return None
    except sqlite3.Error as error:
        print(f"A database error occurred while fetching the users: {error}")
        return None
    

    