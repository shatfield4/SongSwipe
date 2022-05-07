import sqlite3
from Artist import Artist 

con = sqlite3.connect('database.db')

c = con.cursor()

c.execute("""CREATE TABLE selected_artists ( 
            artist_id text,
            followers integer,
            url text,
            genre1 text,
            genre2 text,
            genre3 text, 
            genre4 text,
            genre5 text)""")

c.execute("""CREATE TABLE unselected_artists ( 
            artist_id text,
            genre1 text,
            genre2 text,
            genre3 text, 
            genre4 text,
            genre5 text)""")

con.commit()
con.close()