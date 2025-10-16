from sqlite3 import Cursor
import sqlite3

def get_airlines_data (cursor:Cursor):
    cursor.execute("SELECT * FROM Airlines", [])
    noms_colonnes = [description[0] for description in cursor.description]
    lignes = cursor.fetchall()
    resultat = []
    for i in range(len(lignes)): 
        result = dict(zip(noms_colonnes,lignes[i]))
        resultat.append(result)
    return resultat

def get_airlines_by_country(cursor: Cursor, iso_code: str) -> list[dict] | None:
    resultat = get_airlines_data(cursor)
    liste_r = []
    for i in range(len(resultat)): 
        if resultat[i]["airline_iso2_country"] == iso_code: 
            liste_r.append(resultat[i]["airline_name"])
    if liste_r == [] : 
        return None
    return liste_r


def get_airline_by_id(cursor: Cursor, id: str) -> dict | None:
    resultat = get_airlines_data(cursor)
    for i in range(len(resultat)):
        if i == id : 
            return resultat[i]["airline_name"]
    return None


def remove_airline_by_id(cursor: Cursor, id: str) -> bool:
    resultat = get_airlines_data(cursor)
    for i in range(len(resultat)): 
        if i == id : 
            try :
                cursor.execute(f"DELET FROM Airlines WHERE airline_name = {resultat[i]["airline_name"]} and airline_iso2_country = {resultat[i]["airline_iso2_country"]}")
                resultat.pop(i)
                
            
            except sqlite3.Error as error:
                print("An error occurred while inserting in the table City: {}".format(error))
                # IMPORTANT : we rollback the transaction! No table is created in the database.
                # Return False to indicate that something went wrong.
                return False
    return True
            

    

