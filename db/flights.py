from sqlite3 import Cursor
import sqlite3

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
    cursor.execute("SELECT * FROM Flights", [])
    lignes = cursor.fetchall()
    try : 
        cursor.execute(f"INSERT INTO Flights VALUES ({len(lignes)+1},{price},{departure},{arrival},{airline_icao},{src_icao},{dest_icao},{plane_icao})")
        return True
    except sqlite3.Error as error : 
        print("An error occuried when inserting values :", format(error))
        return False  

def get_flights_data (cursor :Cursor):
    cursor.execute("SELECT * FROM Flights", [])
    noms_colonnes = [description[0] for description in cursor.description]
    lignes = cursor.fetchall()
    resultat = []
    for i in range(len(lignes)): 
        result = dict(zip(noms_colonnes,lignes[i]))
        resultat.append(result)
    return resultat


def get_flight_by_id(cursor: Cursor, flight_id: int) -> dict | None:
    resultat = get_flights_data(cursor)
    for i in range(resultat): 
        if resultat[i]["flight_id"] == flight_id :
            return resultat[i]
    return None 


def remove_flight_by_id(cursor: Cursor, flight_id: int) -> bool:
    resultat = get_flights_data(cursor)
    try : 
        cursor.execute(f"DELETE FROM Flights WHERE flight_id = {flight_id}")
        return True
    except sqlite3.Error as error: 
        print("Erreur :", format(error))
        return False


def get_flights_by_src_city_and_dest_city(
    cursor: Cursor, src_city: str, dest_city: str
) -> list[dict] | None:
    resultat = get_flights_data(cursor)
    lst_r = []
    for i in range(len(resultat)): 
        if resultat[i]["flight_src"] == src_city and resultat[i]["flight_dst"] == dest_city:
            lst_r.append(resultat[i])
    if lst_r == [] : 
        return None
    return lst_r

    
