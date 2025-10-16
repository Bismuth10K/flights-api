from sqlite3 import Cursor


def get_all_countries(cursor: Cursor) -> list[dict]:
    cursor.execute("SELECT * FROM Country", [])
    noms_colonnes = [description[0] for description in cursor.description]
    lignes = cursor.fetchall()
    resultat = []
    for elem in lignes: 
        result = dict(zip(noms_colonnes,elem))
        resultat.append(result)
    return resultat    

def get_all_countries_sorted_by_name(cursor: Cursor, ascending: bool) -> list[dict]:
    resultat = get_all_countries(cursor)
    res = sorted(resultat,key = lambda d: d["airport_country_name"])
    print(res)
    return res


def get_country_name_by_code(cursor: Cursor, iso_code: str) -> str | None:
    resultat = get_all_countries(cursor)
    res = {}
    for i in range(len(resultat)):
        res[resultat[i]["airport_country_code"]] = resultat[i]["airport_country_name"]
    print(iso_code)
    print(res[iso_code])

