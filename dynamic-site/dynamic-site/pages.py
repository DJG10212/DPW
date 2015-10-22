class Page(object):
    def __init__(self):
        pass


    def main_view(self):
        return open("Pages/index.html").read().format(**locals())