import sqlite3

connection = sqlite3.connect("database/game_collector.db")

with open("database/schema.sql") as file:
    connection.executescript(file.read())
    
connection.close()