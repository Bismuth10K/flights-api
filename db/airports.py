from sqlite3 import Cursor
def get_airport_data (cursor : Cursor):
    cursor.execute("SELECT * FROM Airports", [])
    noms_colonnes = [description[0] for description in cursor.description]
    lignes = cursor.fetchall()
    resultat = []
    for i in range(len(lignes)): 
        result = dict(zip(noms_colonnes,lignes[i]))
        resultat.append(result)
    return resultat

def get_airport_id_by_icao(cursor: Cursor, icao: str) -> int | None:
    resultat = get_airport_data(cursor)
    for i in range(len(resultat)): 
        if resultat[i]["airport_icao_code"] == icao: 
            return resultat[i]["airport_id"]
    return None


def get_all_airport_info_by_id(cursor: Cursor, id: int) -> dict | None:
    resultat = get_airport_data(cursor)
    for i in range(len(resultat)): 
        if resultat[i]["airport_id"] == str(id): 
            return resultat[i].values()
    return None
