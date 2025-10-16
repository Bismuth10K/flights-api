from sqlite3 import Cursor
import sqlite3

def get_city_data (cursor : Cursor):
    cursor.execute("SELECT * FROM City", [])
    noms_colonnes = [description[0] for description in cursor.description]
    lignes = cursor.fetchall()
    resultat = []
    for i in range(len(lignes)): 
        result = dict(zip(noms_colonnes,lignes[i]))
        resultat.append(result)
    return resultat


def insert_city(cursor: Cursor, city_name: str, iso_country: str) -> bool:
    cursor.execute("BEGIN")
    resultat = get_city_data(cursor)
    try :
        val = "(" + "'" + str(len(resultat))+ "'"+ ","+ "'" + str(city_name)+ "'" + ',' + "'"+ str(iso_country) + "'" +')'
        print(val)
        cursor.execute(f"INSERT INTO City VALUES {val}")
        return True
    
    except sqlite3.Error as error:
        print("An error occurred while inserting in the table City: {}".format(error))
        # IMPORTANT : we rollback the transaction! No table is created in the database.
        # Return False to indicate that something went wrong.
        return False


def get_city_id_by_name_and_country_code(cursor: Cursor, name: str, iso_code: str) -> int | None:
    resultat = get_city_data(cursor)
    for j in range(len(resultat)):
        if resultat[j]["airport_city_name"] == name and resultat[j]["airport_country_code"] == iso_code:
            return resultat[j]["city_id"]
    return False


def get_city_name_by_id(cursor: Cursor, id: str) -> str | None:
    resultat = get_city_data(cursor)
    for j in range(len(resultat)): 
        if resultat[j]["city_id"] == id : 
            return resultat[j]["airport_city_name"], resultat[j]["airport_country_code"]
    return False


def update_city_name(cursor: Cursor, id: str, new_name: str) -> bool:
    try :
        val = "'" + new_name + "'"
        cursor.execute(f"UPDATE City SET airport_city_name = {val} WHERE city_id = {id}")
        return True
    
    except sqlite3.Error as error:
        print("An error occurred while updating in the table City: {}".format(error))
        # IMPORTANT : we rollback the transaction! No table is created in the database.
        # Return False to indicate that something went wrong.
        return False