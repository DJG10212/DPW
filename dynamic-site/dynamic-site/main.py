
import webapp2
from data import *  # grabs classes from data.py
from pages import *  # grabs all classes from the pages.py page


class MainHandler(webapp2.RequestHandler):
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
        elif self.request.get("movie") == "Ultron":
            response_page.title = "Age of Ultron"
            top_movie.director = "Joss Whedon"
            top_movie.description = "When Tony Stark (Robert Downey Jr.) jump-starts a dormant peacekeeping program, things go terribly awry, forcing him, Thor (Chris Hemsworth), the Incredible Hulk (Mark Ruffalo) and the rest of the Avengers to reassemble. As the fate of Earth hangs in the balance, the team is put to the ultimate test as they battle Ultron, a technological terror hell-bent on human extinction. Along the way, they encounter two mysterious and powerful newcomers, Pietro and Wanda Maximoff."
            top_movie.main_cast = "Robert Downey Jr., Chris Evans, Scarlett Johansson, Chris Hemsworth, Mark Ruffalo"
            top_movie.image_name = "ultron.jpg"
            response_page.movie = top_movie
        elif self.request.get("movie") == "Ironman-3":
            response_page.title = "Ironman 3"
            top_movie.director = "Shane Black"
            top_movie.description = "Plagued with worry and insomnia since saving New York from destruction, Tony Stark (Robert Downey Jr.), now, is more dependent on the suits that give him his Iron Man persona -- so much so that every aspect of his life is affected, including his relationship with Pepper (Gwyneth Paltrow). After a malevolent enemy known as the Mandarin (Ben Kingsley) reduces his personal world to rubble, Tony must rely solely on instinct and ingenuity to avenge his losses and protect the people he loves."
            top_movie.main_cast = "Robert Downey Jr., Gwyneth Paltrow"
            top_movie.image_name = "ironman.jpg"
            response_page.movie = top_movie
        elif self.request.get("movie") == "Dark-Knight-Rises":
            response_page.title = "Dark Knight Rises"
            top_movie.director = "Christopher Nolan"
            top_movie.description = "It has been eight years since Batman (Christian Bale), in collusion with Commissioner Gordon (Gary Oldman), vanished into the night. Assuming responsibility for the death of Harvey Dent, Batman sacrificed everything for what he and Gordon hoped would be the greater good. However, the arrival of a cunning cat burglar (Anne Hathaway) and a merciless terrorist named Bane (Tom Hardy) force Batman out of exile and into a battle he may not be able to win."
            top_movie.main_cast = "Christian Bale, Tom Hardy, Anne Hathaway"
            top_movie.image_name = "batman.jpg"
            response_page.movie = top_movie
        self.response.write(response_page.main_view())  # sends view to user

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
