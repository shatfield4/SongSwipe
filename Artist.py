class Artist:
    
    
    def __init__(self, name, genre_id):
        self.name = name
        self.genre_id = genre_id
    
    
    def getArtist(self, id):
        pass
        
        
    def __repr__(self):
        return "Artist('{}', '{}')".format(self.name, self.genre_id)