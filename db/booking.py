from sqlite3 import Cursor
import sqlite3

def create_booking(cursor: Cursor, user_name: str, flight_id: int) -> bool:
    cursor.execute(f"CREATE TABLE IF NOT EXISTS Booking(booking_id TEXT PRIMARY KEY, user_name TEXT, flight_id TEXT, FOREIGN KEY (user_name) REFERENCES User(user_name), FOREIGN KEY (flight_id) REFERENCES Flight(flight_id))")
    print("etape 1 OK")
    cursor.execute("SELECT * FROM Booking")
    print("etape 2 OK")
    lignes = cursor.fetchall()
    print("etape 3 OK")
    val = '(' + str(len(lignes)+1) + ',' + user_name + ',' + str(flight_id) + ')'
    cursor.execute(f"INSERT INTO Booking VALUES {val}")
    print("etape 4 OK")
    


def get_usernames_by_flight(cursor: Cursor, flight_id: int) -> list[str] | None:
    cursor.execute(f"SELECT FROM Booking WHERE flight_id = {flight_id}")
    reponse = cursor.fecthall()
    lst_users = []
    for i in range(len(reponse)):
        lst_users.append(reponse[i]["user_name"])
    return lst_users


def get_bookings_by_user(cursor: Cursor, user_name: str) -> list[dict] | None:
    cursor.execute(f"SELECT FROM Booking WHERE user_name = {user_name}")
    reponse = cursor.fetchall()
    lst_booking = []
    for i in range(len(reponse)):
        lst_booking.append(reponse[i]["booking_id"])
    return lst_booking


def delete_booking(cursor: Cursor, user_name: str, flight_id: int) -> bool:
    try : 
        cursor.execute(f"DELETE FROM Booking WHERE user_name = {user_name} and flight_id = {flight_id}")
        return True
    
    except sqlite3.Error() as error: 
        return False 
    
