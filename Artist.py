class Artist:
    
    
    def __init__(self, name, genre_id, popularity):
        self.name = name
        self.genre_id = genre_id
        self.popularity = popularity
    
    
    def getArtist(self, id):
        pass
        
        
    def __repr__(self):
        return "Artist('{}', '{}',  '{}')".format(self.name, self.genre_id, self.popularity)