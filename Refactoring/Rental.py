from Movie import Movie

class Rental():
    def __init__(self,movie, daysRented):
        self.movie = movie
        self.daysRented = daysRented
    def getDaysRented(self):
        return self.daysRented
    def getMovie(self):
        return self.movie
  

