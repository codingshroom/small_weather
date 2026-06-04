import sqlite3


try:
    with sqlite3.connect("data/database.db") as connection:
        print("Created/Opened SQLite database successfully.")
except sqlite3.OperationalError as e:
    print("Failed to open database", e)


cursor = connection.cursor()


TABLES = ["cities", "requests", "profiles", "moonphases", "dates", "weatherdata"]
STATEMENTS = {
    "cities": """
        CREATE TABLE IF NOT EXISTS cities (
            cityID INTEGER PRIMARY KEY, 
            cityName TEXT NOT NULL, 
            latitude FLOAT NOT NULL,
            longitude FLOAT NOT NULL
        )
    """, 
    "requests": """
        CREATE TABLE IF NOT EXISTS requests (
            requestID INTEGER PRIMARY KEY,
            profileID INTEGER,
            cityID INTEGER,
            date DATE,
            FOREIGN KEY(profileID) REFERENCES profiles(profileID)
            FOREIGN KEY(cityID) REFERENCES cities(cityID)
            FOREIGN KEY(date) REFERENCES dates(date)
        )
    """, 
    "profiles": """
        CREATE TABLE IF NOT EXISTS profiles (
            profileID INTEGER PRIMARY KEY,
            profileName TEXT NOT NULL,
            requests []INTEGER - FOREIGN KEY
        )
    """, 
    "moonphases": """
        CREATE TABLE IF NOT EXISTS moonphases (
            moonID INTEGER PRIMARY KEY,
            stage TEXT NOT NULL, 
            illumination INTEGER NOT NULL
        )
    """, 
    "dates": """
        CREATE TABLE IF NOT EXISTS dates (
            date DATE PRIMARY KEY,
            weatherID INTEGER FOREIGN KEY,
            moonID INTEGER FOREIGN KEY
        )
    """, 
   "weatherdata": """
        CREATE TABLE IF NOT EXISTS weatherdata (
            weatherID INTEGER PRIMARY KEY, 
            temperature FLOAT NOT NULL, 
            rain FLOAT NOT NULL
        )
    """, 
}


def main():
    for table in TABLES:
        print(table)
        statement = STATEMENTS[table]
        print(statement)
        cursor.execute(statement)


if __name__ == "__main__":
    main()

