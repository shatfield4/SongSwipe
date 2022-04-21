import sqlite3
from sqlite3 import Error

    
    


if __name__ == '__main__':
    db = sqlite3.connect(r"database.db")
    cursor = db.cursor()
    
    # cursor.execute("""CREATE TABLE artists (
    #                 name text,
    #                 genre text
    #                 )""")
    # cursor.execute("INSERT INTO artists VALUES ('Justin Bieber', 'Kpop')")
    # cursor.execute("SELECT * FROM artists WHERE name='Justin Bieber'")
    # cursor.execute("SELECT * FROM artists WHERE name='Justin Bieber'")
    # print(cursor.fetchall())
    

    
    db.commit()
    db.close()