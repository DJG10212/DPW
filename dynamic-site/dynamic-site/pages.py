class Page(object):
    def __init__(self):
        self._title = None  # page title
        self._view_name = "Welcome"

    def main_view(self):
        self._view = open(str("Pages/{view_name}.html").format(view_name=self._view_name.lower()))
        return self._view.read().format(**locals())  # reads then inserts variables and returns to user

    # getter
    @property
    def view_name(self):
        return self._view_name

    # setter
    @view_name.setter
    def view_name(self, new_name):
        self._view_name = new_name


class ContentPage(Page):
    def __init__(self):
        self._title = "Content Page"
        self._view_name = "Content"
