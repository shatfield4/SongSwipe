class Artist:
    
    
<<<<<<< Updated upstream
    def __init__(self, name, genre_id, popularity):
        self.name = name
        self.genre_id = genre_id
        self.popularity = popularity
=======
    def __init__(self, name, genre_id, followers, image_url):
        self.name = name
        self.genre_id = genre_id
        self.followers = followers
        self.image_url = image_url
>>>>>>> Stashed changes
    
    
    def getArtist(self, id):
        pass
        
        
    def __repr__(self):
        return "Artist('{}', '{}',  '{}')".format(self.name, self.genre_id, self.popularity)