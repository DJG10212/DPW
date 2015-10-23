
import webapp2
from data import *  # grabs classes from data.py
from pages import *  # grabs all classes from the pages.py page


class MainHandler(webapp2.RequestHandler):
    def get(self):
        if not self.request.GET:
            # user hasn't requested info. show standard landing page
            response_page = Page()
            response_page.title = "Top Movies"
        else:
            # user has requested info. Show user requested movie page
            response_page = MoviePage()  # creates a MoviePage instance
            top_movie = Data()
            top_movie.movie_name = self.request.get("movie")
            response_page.movie = top_movie.movie
        self.response.write(response_page.main_view())  # sends view to user

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
