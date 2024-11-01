class Movie:
    def __init__(self,title,director,releaseDate,overview,rating):
        self.title = title
        self.director = director
        self.releaseDate = releaseDate
        self.overview = overview
        self.rating = rating
        
    def getTitle(self):
        return self.title
    
    def getDirector(self):
        return self.director
    
    def getReleaseDate(self):
        return self.releaseDate
    
    def getOverview(self):
        return self.overview
    
    def getRating(self):
        return self.rating