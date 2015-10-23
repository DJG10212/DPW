
import webapp2
from data import *  # grabs classes from data.py
from pages import *  # grabs all classes from the pages.py page


class MainconsHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.GET:
            # user has submitted get, so we show the right info
            response_page = MoviePage()
            top_movie = Movie()
        else:
            # the user hasn't requested info
            response_page = Page()
            response_page.title = "Credit"
        if self.request.get("movie") == "Jurassic-World":
            response_page.title = "Jurassic World"
            top_movie.director = "Colin Trevorrow"
            top_movie.description = "Located off the coast of Costa Rica, the Jurassic World luxury resort provides a habitat for an array of genetically engineered dinosaurs, including the vicious and intelligent Indominus rex. When the massive creature escapes, it sets off a chain reaction that causes the other dinos to run amok. Now, it's up to a former military man and animal expert (Chris Pratt) to use his special skills to save two young brothers and the rest of the tourists from an all-out, prehistoric assault."
            top_movie.main_cast = "Bryce Dallas Howard, Chris Pratt"
            top_movie.image_name = "jurassicWorld.jpg"
            response_page.movie = top_movie
        elif self.request.get("movie") == "The-Avengers":
            response_page.title = "The Avengers"
            top_movie.director = "Joss Whedon"
            top_movie.description = "When Thor's evil brother, Loki (Tom Hiddleston), gains access to the unlimited power of the energy cube called the Tesseract, Nick Fury (Samuel L. Jackson), director of S.H.I.E.L.D., initiates a superhero recruitment effort to defeat the unprecedented threat to Earth. Joining Fury's "dream team" are Iron Man (Robert Downey Jr.), Captain America (Chris Evans), the Hulk (Mark Ruffalo), Thor (Chris Hemsworth), the Black Widow (Scarlett Johansson) and Hawkeye (Jeremy Renner)."
            top_movie.main_cast = "Robert Downey Jr., Chris Evans, Scarlett Johansson, Chris Hemsworth, Mark Ruffalo"
            top_movie.image_name = "theAvengers.jpg"
            response_page.movie = top_movie
        self.response.write(landing_page.main_view())  # sends view to user

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
