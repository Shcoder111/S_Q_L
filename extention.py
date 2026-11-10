import sqlite3
import pandas as pd

connect = sqlite3.connect("movies.db")
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE IF NOT EXISTS Movie 
    Movie_id       INTEGER PRIMARY KEY,
    Title          TEXT,
    GENRE          TEXT,
    Year           TEXT,
    Rating         REAL,
    Duration       INTEGER
);

CREATE TABLE IF NOT EXISTS Actor (
    Actor_id      INTERGER       PRIMARY KEY,
    Actor_Name    TEXT,
    Birth_Year    INTEGER,
    Country       TEXT
);

CREATE TABLE IF NOT EXISTS Movie_Actor (
    Movie_id INTEGER,
    Actor_id INTEGER,
);
""")

cursor.execute("DELETE FROM Movie")

cursor.executemany(""" 
INSERT INTO Movie VALUES (?, ?, ?, ?, ?, ?)
""", [
    (1, 'The Amazing Spiderman',   'Action', 2012, 8.5, 89),
    (2, 'The Amazing Spiderman 2', 'Action', 2014, 8.3, 81),
    (3, 'The Spiderman',           'Action', 2002, 7.9, 1331),
    (4, 'Avengers : Endgame'     , 'Action', 2026, 9.9, 89),
    (5, 'Avengers : Doomsday'  ,   'Action', 2026, 9.9, 8899),
    (6, 'Sonic The Hedgehog 3'   , 'Action', 2024, 7.2, 1381),
    (7, 'Avengers : Infinity War', 'Action', 2002, 7.9, 131),
    (8, 'Spiderman : No way Home', 'Action', 2024, 8.9, 88),
    (9, 'Spiderman : Homecoming' , 'Action', 2010, 8.9, 86),
    (10,'Spiderman : Brand New Day','Action', 2026, 9.9, 889),
    (11, 'Sonic The Hedgehog 4'   , 'Action', 2027, 7.6, 1181),
    (12, 'Spiderman : The Darkest Day', 'Action', 2027, 10.0, 121)
])

conn.commit()
print("\n Unique Genres _-_-_-_")
print(pd.read_sql_query(
    "SELECT DISTINCT Genre FROM Movie", conn
))

print("\n Highest rated Movies _-_-_-_")
print(pd.read_sql_query(
    "SELECT Title,Rating FROM Movie BY Rating DESC", conn
))

print("\n Oldest Movies _-_-_-_")
print(pd.read_sql_query(
    "SELECT Title,Rating FROM Movie BY Year ASC", conn
))

print("\n Number of Action Movies _-_-_-_")
print(pd.read_sql_query(
    "SELECT COUNT(*) FROM Movie WHERE Genre = 'Action'", conn
))

print("\n Total Animation Duration _-_-_-_")
print(pd.read_sql_query(
    "SELECT SUM(Duration) FROM Movie WHERE Genre = 'Animation'", conn
))

print("\n Average rating _-_-_-_")
print(pd.read_sql_query(
    "SELECT AVG(Rating) FROM Movie", conn
))

print("\n Average Action Movie Duration _-_-_-_")
print(pd.read_sql_query(
    "SELECT AVG(Duration) FROM Movie WHERE Genre = 'Action'", conn
))

print("\n Movies in Each Genre _-_-_-_")
print(pd.read_sql_query(
    "SELECT GENRE, COUNT(*) FROM Movie GROUP BY Genre ", conn
))

print("\n Average Rating by Genre _-_-_-_")
print(pd.read_sql_query(
    "SELECT GENRE, COUNT(*) FROM Movie GROUP BY Genre ORDER BY AVG(Rating) DESC", conn
))

conn.close()
print("\n\n\n Database Closed")