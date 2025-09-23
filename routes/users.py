from flask import Blueprint, request, jsonify

from db import get_db_connexion, close_db_connexion

import db.users

users_bp = Blueprint("users", __name__)


@users_bp.route("/", methods=["GET"])
def get_all_users():
    """Fetch all users from the database.

    Returns
    -------
    status_code
        200 by default if no error occured
        500 if an error occured while fetching the users
    data
        users as a json if no error occurs (can be empty if no users)
        an error message if an error occured while fetching the users.
    """
    conn = get_db_connexion()
    cursor = conn.cursor()

    all_users = db.users.get_users(cursor)
    if all_users == None:
        conn.rollback()
        close_db_connexion(cursor, conn)
        return "Error: while fetching users", 500
    conn.commit()
    close_db_connexion(cursor, conn)
    return jsonify({"users": [dict(user)["username"] for user in all_users]})


@users_bp.route("/<user_name>", methods=["GET"])
def get_user(user_name):
    """Fetch a single user from the database based on its username.

    Parameters
    ----------
    user_name
        username of the user (as defined in the database)

    Returns
    -------
    data
        user as a json if the user is in the database
        an error message "This user does not exists" if the user requested
            is not in the database
        an error message "Error: while fetching user" if an error occured
            while fetching the user.
    status_code
        200 if the user is correctly fetched
        404 if the query to the database was a success but the user
                is not in the database
        500 if an error occured while fetching the user
    """
    # TODO
    return jsonify({"message": "TODO"})


@users_bp.route("/<user_name>", methods=["PATCH"])
def patch_password(user_name):
    """Patch the password of an user.
    The password must be passed in the data of the POST request.

    Parameters
    ----------
    user_name
        username of the user (as defined in the database)

    Returns
    -------
    data
        user as a json if the user is in the database
        a message "Password not provided" if the password is not in
            the request
        an error message "Error: while updating password" if an error
            occured while updating the password.
    status_code
        200 if the password is correctly modified
        404 if no password is provided in the request
        500 if an error occured while updating the password
    """
    # TODO
    return jsonify({"message": "TODO"})


@users_bp.route("/", methods=["POST"])
def add_user():
    """Add an user to the database.
    The username and password must be passed in the data of the POST request.

    Returns
    -------
    data
        a message "Done" if the user is correctly added
        a message "Username or password not provided" if the password or
            username is not in the data of the POST request
        an error message "Error: while adding a new user" if an error occured
            while updating the password
    status_code
        200 if the user was added to the database
        404 if no username and password are provided in the request
        500 if an error occured while updating the password
    """
    # TODO
    return jsonify({"message": "TODO"})
