class Page(object):
    def __init__(self):
        self._title = None  # page title

    def main_view(self):
        return open("Pages/Credit.html").read()  # reads page and returns

    # getter
    @property
    def title(self):
        return self._title


    # setter
    @title.setter
    def title(selfself, new_title):
        self._title = new_title


class MoviePage(Page):
    def __init__(self):
        self._movie = None  # movie objects

    def render_view(self):
        return open("Pages/Content.html").read().format(**locals())

    # getter
    @property
    def movie(self, new_movie):
        self._movie = new_movie