class Data(object):
    def __init__(self):
        self._title = None  # movie title
        self._time = None  # when the movie was in theaters


class Movie(Data):
    def __init__(self):
        self._director = None  # director of the movies name
        self._description = None  # movies description
        self._main_cast = None  # movies leading cast
        self._image_path = None  # image location
