class Data(object):
    def __init__(self):
        self._title = None  # movie title
        self._director = None
        self._movie_name = None
        self._movie = Movie()

    # getter
    @property
    def movie_name(self):
        return self._movie_name

    @property
    def movie(self):
        return self._movie

    # setter
    @movie_name.setter
    def movie_name(self, new_movie_name):
        self._movie_name = new_movie_name
        if self._movie_name == "Jurassic-World":
            self._movie._title = self._movie_name
            self._movie._director = "Colin Trevorrow"
            self._movie._description = "Located off the coast of Costa Rica, the Jurassic World luxury resort provides a habitat for an array of genetically engineered dinosaurs, including the vicious and intelligent Indominus rex. When the massive creature escapes, it sets off a chain reaction that causes the other dinos to run amok. Now, it's up to a former military man and animal expert (Chris Pratt) to use his special skills to save two young brothers and the rest of the tourists from an all-out, prehistoric assault."
            self._movie._main_cast = "Bryce Dallas Howard, Chris Pratt"
            self._movie._image_name = "jurassicWorld.jpg"
        elif self._movie_name == "The-Avengers":
            self._movie._title = self._movie_name
            self._movie._director = "Joss Whedon"
            self._movie._description = "Avengers description here"
            self._movie._main_cast = "Robert Downey Jr., Chris Evans, Scarlett Johansson, Chris Hemsworth, Mark Ruffalo"
            self._movie._image_name = "theAvengers.jpg"
        elif self._movie_name == "Ultron":
            self._movie._title = self._movie_name
            self._movie._director = "Joss Whedon"
            self._movie._description = "When Tony Stark (Robert Downey Jr.) jump-starts a dormant peacekeeping program, things go terribly awry, forcing him, Thor (Chris Hemsworth), the Incredible Hulk (Mark Ruffalo) and the rest of the Avengers to reassemble. As the fate of Earth hangs in the balance, the team is put to the ultimate test as they battle Ultron, a technological terror hell-bent on human extinction. Along the way, they encounter two mysterious and powerful newcomers, Pietro and Wanda Maximoff."
            self._movie._main_cast = "Robert Downey Jr., Chris Evans, Scarlett Johansson, Chris Hemsworth, Mark Ruffalo"
            self._movie._image_name = "ultron.jpg"
        elif self._movie_name == "Ironman-3":
            self._movie._title = self._movie_name
            self._movie._director = "Shane Black"
            self._movie._description = "Plagued with worry and insomnia since saving New York from destruction, Tony Stark (Robert Downey Jr.), now, is more dependent on the suits that give him his Iron Man persona -- so much so that every aspect of his life is affected, including his relationship with Pepper (Gwyneth Paltrow). After a malevolent enemy known as the Mandarin (Ben Kingsley) reduces his personal world to rubble, Tony must rely solely on instinct and ingenuity to avenge his losses and protect the people he loves."
            self._movie._main_cast = "Robert Downey Jr., Gwyneth Paltrow"
            self._movie._image_name = "ironman.jpg"
        elif self._movie_name == "Dark-Knight-Rises":
            self._movie._title = self._movie_name
            self._movie._director = "Christopher Nolan"
            self._movie._description = "It has been eight years since Batman (Christian Bale), in collusion with Commissioner Gordon (Gary Oldman), vanished into the night. Assuming responsibility for the death of Harvey Dent, Batman sacrificed everything for what he and Gordon hoped would be the greater good. However, the arrival of a cunning cat burglar (Anne Hathaway) and a merciless terrorist named Bane (Tom Hardy) force Batman out of exile and into a battle he may not be able to win."
            self._movie._main_cast = "Christian Bale, Tom Hardy, Anne Hathaway"
            self._movie._image_name = "batman.jpg"


class Movie(Data):
    def __init__(self):
        self._title = None  # title of movie
        self._director = None  # director of the movies name
        self._description = None  # movies description
        self._main_cast = None  # movies leading cast
        self._image_name = None  # image location
