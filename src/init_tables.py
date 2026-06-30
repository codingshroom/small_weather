import sqlite3


TABLES = ["profiles", "cities", "weatherdata", "moonphases", "dates", "requests"]
STATEMENTS = {
    "cities": """
        CREATE TABLE IF NOT EXISTS cities (
            cityID INTEGER PRIMARY KEY,
            cityName TEXT NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL
        )
    """,
    "requests": """
        CREATE TABLE IF NOT EXISTS requests (
            requestID INTEGER PRIMARY KEY,
            profileID INTEGER NOT NULL,
            cityID INTEGER NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY(profileID) REFERENCES profiles(profileID),
            FOREIGN KEY(cityID) REFERENCES cities(cityID),
            FOREIGN KEY(date) REFERENCES dates(date)
        )
    """,
    "profiles": """
        CREATE TABLE IF NOT EXISTS profiles (
            profileID INTEGER PRIMARY KEY,
            profileName TEXT NOT NULL
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
            date TEXT PRIMARY KEY,
            moonID INTEGER NOT NULL,
            FOREIGN KEY(moonID) REFERENCES moonphases(moonID)
        )
    """,
   "weatherdata": """
        CREATE TABLE IF NOT EXISTS weatherdata (
            cityID INTEGER
            date TEXT
            hour INTEGER
            temperature REAL NOT NULL,
            rainProbability REAL NOT NULL,
            rainAmount REAL NOT NULL
            PRIMARY KEY(cityID, date, hour)
            FOREIGN KEY(cityID) REFERENCES cities(cityID)
            FOREIGN KEY(date) REFERENCES dates(date)
        )
    """,
}


def main():
    try:
        with sqlite3.connect("data/test.db") as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            cursor = connection.cursor()
            print("Created/Opened SQLite database successfully.")
            for table in TABLES:
                print(table)
                statement = STATEMENTS[table]
                cursor.execute(statement)
                connection.commit()
    except sqlite3.OperationalError as e:
        print("Failed to open database", e)


if __name__ == "__main__":
    main()

