class Data(object):
    def __init__(self):
        self._title = None  # movie title
        self._movie = Movie()

    # getter
    @property
    def title(self):
        return self._title

    @property
    def movie(self):
        return self._movie

    # setter
    @title.setter
    def title(self, new_title):
        if self._title == "Jurassic-World":
            self._movie.title = "Jurassic World"
            self._movie.director = "Colin Trevorrow"
            self._movie.description = "Located off the coast of Costa Rica, the Jurassic World luxury resort provides a habitat for an array of genetically engineered dinosaurs, including the vicious and intelligent Indominus rex. When the massive creature escapes, it sets off a chain reaction that causes the other dinos to run amok. Now, it's up to a former military man and animal expert (Chris Pratt) to use his special skills to save two young brothers and the rest of the tourists from an all-out, prehistoric assault."
            self._movie.main_cast = "Bryce Dallas Howard, Chris Pratt"
            self._movie.image_name = "jurassicWorld.jpg"
        elif self._title == "The-Avengers":
            self._movie.title = "The Avengers"
            self._movie.director = "Joss Whedon"
            self._movie.description = "Avengers description here"
            self._movie.main_cast = "Robert Downey Jr., Chris Evans, Scarlett Johansson, Chris Hemsworth, Mark Ruffalo"
            self._movie.image_name = "theAvengers.jpg"
        elif self._title == "Ultron":
            self._movie.title = "Age of Ultron"
            self._movie.director = "Joss Whedon"
            self._movie.description = "When Tony Stark (Robert Downey Jr.) jump-starts a dormant peacekeeping program, things go terribly awry, forcing him, Thor (Chris Hemsworth), the Incredible Hulk (Mark Ruffalo) and the rest of the Avengers to reassemble. As the fate of Earth hangs in the balance, the team is put to the ultimate test as they battle Ultron, a technological terror hell-bent on human extinction. Along the way, they encounter two mysterious and powerful newcomers, Pietro and Wanda Maximoff."
            self._movie.main_cast = "Robert Downey Jr., Chris Evans, Scarlett Johansson, Chris Hemsworth, Mark Ruffalo"
            self._movie.image_name = "ultron.jpg"
        elif self._title == "Ironman-3":
            self._movie.title = "Ironman 3"
            self._movie.director = "Shane Black"
            self._movie.description = "Plagued with worry and insomnia since saving New York from destruction, Tony Stark (Robert Downey Jr.), now, is more dependent on the suits that give him his Iron Man persona -- so much so that every aspect of his life is affected, including his relationship with Pepper (Gwyneth Paltrow). After a malevolent enemy known as the Mandarin (Ben Kingsley) reduces his personal world to rubble, Tony must rely solely on instinct and ingenuity to avenge his losses and protect the people he loves."
            self._movie.main_cast = "Robert Downey Jr., Gwyneth Paltrow"
            self._movie.image_name = "ironman.jpg"
        elif self._title == "Dark-Knight-Rises":
            self._movie.title = "Dark Knight Rises"
            self._movie.director = "Christopher Nolan"
            self._movie.description = "It has been eight years since Batman (Christian Bale), in collusion with Commissioner Gordon (Gary Oldman), vanished into the night. Assuming responsibility for the death of Harvey Dent, Batman sacrificed everything for what he and Gordon hoped would be the greater good. However, the arrival of a cunning cat burglar (Anne Hathaway) and a merciless terrorist named Bane (Tom Hardy) force Batman out of exile and into a battle he may not be able to win."
            self._movie.main_cast = "Christian Bale, Tom Hardy, Anne Hathaway"
            self._movie.image_name = "batman.jpg"
        self._title = new_title


class Movie(Data):
    def __init__(self):
        self._director = None  # director of the movies name
        self._description = None  # movies description
        self._main_cast = None  # movies leading cast
        self._image_path = None  # image location
