
import webapp2
from data import *  # grabs classes from data.py
from pages import *  # grabs all classes from the pages.py page


class MainHandler(webapp2.RequestHandler):
    def get(self):
        landing_page = MoviePage()  # creates an instance of Page
        top_movie = Movie()
        if self.request.get("movie") == "Jurassic-World":
            landing_page.title = "Jurassic World"
            landing_page.view_name = "jurassicWorld"
            top_movie.director = "Colin Trevorrow"
            top_movie.description = "Located off the coast of Costa Rica, the Jurassic World luxury resort provides a habitat for an array of genetically engineered dinosaurs, including the vicious and intelligent Indominus rex. When the massive creature escapes, it sets off a chain reaction that causes the other dinos to run amok. Now, it's up to a former military man and animal expert (Chris Pratt) to use his special skills to save two young brothers and the rest of the tourists from an all-out, prehistoric assault."
            top_movie.main_cast = "Bryce Dallas Howard, Chris Pratt"
            top_movie.image_name = "jurassicWorld.jpg"
            landing_page.movie = top_movie
        else:
            landing_page.title = "Credit"
            landing_page.view_name = "Credit"
        self.response.write(landing_page.main_view())  # sends view to user

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
