import sqlite3
from sqlite3 import Error

    
class Sqlite_test:
    
    
    def __init__(self, database):
        self.database = database
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        
             
             
    def addToArtist(self, name, genre_id):
        self.cursor.execute("INSERT INTO artists VALUES ('{}', '{}')".format(name, genre_id))
        self.connection.commit()
        self.connection.close()









#     db = sqlite3.connect(r"database.db")
#     cursor = db.cursor()
    
#     # cursor.execute("DELETE FROM artists WHERE name='Justin Bieber'")
#     # cursor.execute("""CREATE TABLE artists (
#     #                 name text,
#     #                 genre text
#     #                 )""")
#     # cursor.execute("INSERT INTO artists VALUES ('Justin Bieber', 'Kpop')")
#     # cursor.execute("SELECT * FROM artists WHERE name='Justin Bieber'")
#     # cursor.execute("SELECT * FROM artists WHERE name='Justin Bieber'")
#     # print(cursor.fetchall())
    
#     db.commit()
#     db.close()