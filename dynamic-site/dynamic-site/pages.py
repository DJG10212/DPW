class Page(object):
    def __init__(self):
        self._title = None  # page title

    def main_view(self):
        return open("pages/index.html").read().format(**locals())  # reads page and returns

    # getter
    @property
    def title(self):
        return self._title

    # setter
    @title.setter
    def title(self, new_title):
        self._title = new_title


class MoviePage(Page):
    def __init__(self):
        self._movie = None  # movie objects

    def main_view(self):
        return open("pages/content.html").read().format(**locals())  # reads page and returns

    # getter
    @property
    def movie(self):
        return self._movie

    # setter
    @movie.setter
    def movie(self, new_movie):
        self._movie = new_movie


