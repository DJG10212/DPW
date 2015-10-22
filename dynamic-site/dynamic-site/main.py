
import webapp2
from pages import *  # grabs all classes from the pages.py page


class MainHandler(webapp2.RequestHandler):
    def get(self):
        landing_page = ContentPage()  # creates an instance of Page
        self.response.write(landing_page.main_view("index"))  # sends view to user

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
