class Page(object):
    def __init__(self):
        self._title = None  # page title
        self._view_name = "Welcome"

    def main_view(self):
        self._view = open(str("Pages/{view_name}.html").format(view_name=self._view_name.lower()))
        return self._view.read().format(**locals())  # reads then inserts variables and returns to user

    # getter
    @property
    def title(self):
        return self._title

    @property
    def view_name(self):
        return self._view_name

    # setter
    @title.setter
    def title(selfself, new_title):
        self._title = new_title

    @view_name.setter
    def view_name(self, new_view_name):
        self._view_name = new_view_name


class MoviePage(Page):
    def __init__(self):
        self._movie = None  # movie objects

    # getter
    @property
    def movie(self, new_movie):
        self._movie = new_movie