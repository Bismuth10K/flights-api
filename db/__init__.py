import sqlite3
import utils
import pandas as pd
from sqlalchemy import create_engine 
from db.booking import *




def split_data(csv_file: str):
    table = pd.read_csv(csv_file, header = 0)
    """
    print(table.head(10))
    print("\t ------------")
    print (table.info())
    print("\t ------------")
    print(table["airline_name"])
    """
    return table


def transform_data(csv_file: str):
    """
        Preprocess the data before adding it to the database,
        e.g delete useless or rename columns

    """
    table = split_data(csv_file)
    
    table_airlines = table[["airline_ICAO","airline_name","airline_iso2_country"]]
    table_flights = table[["flight_price_usd","flight_departure", "flight_arrival","flight_airline_icao","flight_src","flight_dst","flight_plane"]]
    table_aircraft = table[["plane_icao","plane_name"]]
    table_airport = table[["airport_icao_code","airport_type","airport_lat","airport_lon","airport_city_name","airport_country_code"]]
    table_country = table[["airport_country_code","airport_country_name"]]
    table_city = table[["airport_city_name","airport_country_code"]]
    table_aircraft.dropna(axis = 0,how = 'all',inplace = True)
    table_airlines.dropna(axis = 0,how = 'all',inplace = True)
    table_airport.dropna(axis = 0,how = 'all',inplace = True)
    table_country.dropna(axis = 0,how = 'all',inplace = True)
    table_flights.dropna(axis = 0,how = 'all',inplace = True)
    table_city.dropna(axis = 0,how = 'all',inplace = True)
    table_aircraft.drop_duplicates(subset = "plane_icao",keep = 'first',inplace = True)
    table_airlines.drop_duplicates(subset = "airline_ICAO",keep = 'first',inplace = True)
    table_airport.drop_duplicates(subset = "airport_icao_code",keep = 'first',inplace = True)
    table_country.drop_duplicates(subset = "airport_country_code", keep = 'first',inplace = True)
    table_city.drop_duplicates(subset = "airport_city_name", keep = 'first',inplace = True)
    # print(str(table_flights.iloc[0]))
    lst_table = [table_aircraft,table_airlines,table_airport,table_country,table_flights,table_city]
    """
    print(table_airlines)
    print("\t ---------")
    print(table_flights.head(5))
    print("\t ---------")
    print(table_aircraft.head(5))
    print("\t ---------")
    print(table_airport.head(5))
    print("\t ---------")
    print(table_country.head(5))"""
    return lst_table


def get_db_connexion():
    # Loads the app config into the dictionary app_config.
    app_config = utils.load_config()

    if not app_config:
        print("Error: while loading the app configuration")
        return None

    # From the configuration, gets the path to the database file.
    db_file = app_config["db"]

    # Open a connection to the database.
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row

    return conn


def close_db_connexion(cursor, conn):
    """Close a database connexion and the cursor.

    Parameters
    ----------
    cursor
        The object used to query the database.
    conn
        The object used to manage the database connection.
    """
    cursor.close()
    conn.close()


def create_database(cursor, conn):
    """Creates the flights database

    Parameters
    ----------
    cursor
        The object used to query the database.
    conn
        The object used to manage the database connection.

    Returns
    -------
    bool
        True if the database could be created, False otherwise.
    """

    # We open a transaction.
    # A transaction is a sequence of read/write statements that
    # have a permanent result in the database only if they all succeed.
    #
    # More concretely, in this function we create many tables in the database.
    # The transaction is therefore a sequence of CREATE TABLE statements such as :
    #
    # BEGIN
    # CREATE TABLE XXX
    # CREATE TABLE YYY
    # CREATE TABLE ZZZ
    # ....
    #
    # If no error occurs, all the tables are permanently created in the database.
    # If an error occurs while creating a table (for instance YYY), no table will be created, even those for which
    # the statement CREATE TABLE has already been executed (in this example, XXX).
    #
    # When we start a transaction with the statement BEGIN, we must end it with either COMMIT
    # or ROLLBACK.
    #
    # * COMMIT is called when no error occurs. After calling COMMIT, the result of all the statements in
    # the transaction is permanetly written to the database. In our example, COMMIT results in actually creating all the tables
    # (XXX, YYY, ZZZ, ....)
    #
    # * ROLLBACK is called when any error occurs in the transaction. Calling ROLLBACK means that
    # the database is not modified (in our example, no table is created).
    #
    #
    cursor.execute("BEGIN")

    # Create the tables.
    tables = {
        "User": """
            CREATE TABLE IF NOT EXISTS User(
                username TEXT PRIMARY KEY,
                password BINARY(256)
            );
            """,
        
        "Country" : """CREATE TABLE IF NOT EXISTS Country(airport_country_code TEXT PRIMARY KEY, airport_country_name  TEXT)""",
        "Airlines" : """CREATE TABLE IF NOT EXISTS Airlines(airline_ICAO TEXT PRIMARY KEY, airline_name TEXT,
            airline_iso2_country TEXT)""",

        "Airports" : """CREATE TABLE IF NOT EXISTS Airports(airport_icao_code TEXT PRIMARY KEY, airport_id TEXT, airport_type TEXT, airport_lat INTEGER,
          airport_lon INTEGER, airport_city_name TEXT, airport_country_code TEXT, FOREIGN KEY (airport_country_code) REFERENCES Country(airport_country_code))""",

        "Flights" : """CREATE TABLE IF NOT EXISTS Flights(flight_id INTEGER PRIMARY KEY, flight_price_usd INTEGER, flight_departure TEXT, flight_arrival TEXT, 
            flight_airline_icao TEXT, flight_src TEXT, flight_dst TEXT, flight_plane TEXT)""",
        "Aircrafts" : """CREATE TABLE IF NOT EXISTS Aircrafts(plane_icao TEXT PRIMARY KEY, plane_name  TEXT, FOREIGN KEY (plane_name) REFERENCES Flights(flight_plane))""",
        "City" : """CREATE TABLE IF NOT EXISTS City(city_id TEXT PRIMARY KEY, airport_city_name TEXT, airport_country_code  TEXT)"""
          }
    try:
        # To create the tables, we call the function cursor.execute() and we pass it the
        # CREATE TABLE statement as a parameter.
        # The function cursor.execute() can raise an exception sqlite3.Error.
        # That's why we write the code for creating the tables in a try...except block.
        for tablename in tables:
            print(f"Creating table {tablename}...", end=" ")
            cursor.execute(tables[tablename])
            print("OK")

    # Exception raised when something goes wrong while creating the tables.
    except sqlite3.Error as error:
        print("An error occurred while creating the tables: {}".format(error))
        # IMPORTANT : we rollback the transaction! No table is created in the database.
        conn.rollback()
        # Return False to indicate that something went wrong.
        return False

    # If we arrive here, that means that no error occurred.
    # IMPORTANT : we must COMMIT the transaction, so that all tables are actually created in the database.
    conn.commit()
    print("Database created successfully")
    # Returns True to indicate that everything went well!
    return True


def populate_database(cursor, conn, lst_table):
    cursor.execute("BEGIN")
    table = ["Aircrafts","Airlines","Airports","Country","Flights","City"]
    try:
        # To create the tables, we call the function cursor.execute() and we pass it the
        # CREATE TABLE statement as a parameter.
        # The function cursor.execute() can raise an exception sqlite3.Error.
        # That's why we write the code for creating the tables in a try...except block.
        for j in range(len(table)):
            print(f"Populating table {table[j]}...", end=" ")
            for i in range(len(lst_table[j])): 
                ligne_table = lst_table[j].iloc[i].to_dict()
                # print(type(ligne_table))
                if table[j] == "Flights" or table[j] =="City" : 
                    lst = list(ligne_table.values())
                    lst.insert(0,i)
                    str_ligne = str(lst)
                elif table[j] == "Airports": 
                    lst = list(ligne_table.values())
                    lst.insert(1,i)
                    str_ligne = str(lst)
                else : 
                    str_ligne = str(list(ligne_table.values()))
                str_ligne = str_ligne.replace('[','(')
                str_ligne = str_ligne.replace(']',')')
                # print("\t", str_ligne) 
                cursor.execute(f"INSERT INTO {table[j]} VALUES {str_ligne}")
            print("OK")

    ###################################################################

    # Exception raised when something goes wrong while creating the tables.
    except sqlite3.Error as error:
        print("An error occurred while populating the tables: {}".format(error))
        # IMPORTANT : we rollback the transaction! No table is created in the database.
        #conn.rollback()
        # Return False to indicate that something went wrong.
        return False
    

def init_database():
    """Initialise the database by creating the database
    and populating it.
    """
    #split_data("./data/all.csv")
    lst_table = transform_data("./data/all.csv")
    try:
        conn = get_db_connexion()

        # The cursor is used to execute queries to the database.
        cursor = conn.cursor()

        # Creates the database. THIS IS THE FUNCTION THAT YOU'LL NEED TO MODIFY
        create_database(cursor, conn)

        # Populates the database.
        populate_database(cursor, conn, lst_table)
        
        conn.commit()

        # get_country_name_by_code(cursor,iso_code = "BS")
        # Closes the connection to the database
        close_db_connexion(cursor, conn)

    except Exception as e:
        print("Error: Database cannot be initialised:", e)
