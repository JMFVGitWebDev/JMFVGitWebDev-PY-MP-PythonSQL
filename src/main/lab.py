"""
This lab will explore establishing a database connection via Python and SQLite,
as well as creating a table, inserting data, and selecting that data.
"""
import sqlite3


conn = sqlite3.connect("my_database.db") 
"TODO: Create a database connection"
cursor = conn.cursor() 
"TODO: create a cursor with the connection"


# Create a dogs table with autoincrementing ID
def create_dogs_table():
    cursor.execute("""
CREATE TABLE IF NOT EXISTS dogs (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    breed TEXT,
    age INTEGER
)
""")

    """TODO"""


# TODO: Complete insert_dog() by inserting a new dog (provided in the parameters) into the "dogs" table.
def insert_dog(name, breed, age):

    query = "INSERT INTO dogs (name, breed, age) VALUES (?, ?, ?)"

   

    cursor.execute("INSERT INTO dogs (name, breed, age) VALUES (?, ?, ?)", (name, breed, age))

    """TODO"""


# TODO: Complete select_all_dogs() by selecting all rows from the "dogs" table *and returning them*.
def select_all_dogs():

    # return the rows
    return """TODO"""
