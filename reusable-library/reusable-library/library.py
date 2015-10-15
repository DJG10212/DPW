class FavoriteMovies(objecxt):
    def __init__(self):
        self.__movie_list = []
        # have an array to hold the movie info
        # have some way to add to array of movies
        # generate list of movies
        # calculate time span between movies

    def addMovie(self, m):
        self.__movie_list.append(m)
        print m








class MovieData(object): # Data Object
    def __init__(self):
        self.title = ''
        self.__year = 0 #check for valid year
        self.director = ''

    @property
    def year(self):
        pass

    @year.setter
    def year(self, y):
        if y > 2014: #if the dates not valid
            print "Error, invalid date!"
            self.__year = 2014
        else:
            self.__year = y
