import sqlite3
from sqlite3 import Error

    
class Sqlite_test:
    
    
    def __init__(self, database):
        self.database = database
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        
             
             
    def addToSavedArtists(self, artist_id, genre_id):
        self.cursor.execute("INSERT INTO saved_artists VALUES ('{}', '{}')".format(artist_id, genre_id))
        self.connection.commit()
        self.connection.close()

    def removeArtist(self, artist_id):
        self.cursor.execute("DELETE FROM saved_artists WHERE artist_id='{}'".format(artist_id))
        self.connection.commit()
        self.connection.close()
    
    def addToQueue(self, artist_id):
        self.cursor.execute("INSERT INTO artist_queue VALUES ('{}')".format(artist_id))
        self.connection.commit()
        self.connection.close()

    def removeFromQueue(self,artist_id):
        self.cursor.execute("DELETE FROM artist_queue WHERE artist_id='{}'".format(artist_id))
        self.connection.commit()
        self.connection.close()



#CREATE SAVED_ARTISTS TABLE
#--------------------------------------------------#
# sqlite.cursor.execute("""CREATE TABLE saved_artists (
#                             Artist_id text,
#                             Genre_id text                 
#                             )""")

#CREATE ARTISTS_QUEUE TABLE
#--------------------------------------------------#
# sqlite.cursor.execute("""CREATE TABLE artist_queue (
#                             artist_id text
#                             )""")