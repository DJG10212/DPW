

import webapp2
from pages import Page, ResultsPage


class MainHandler(webapp2.RequestHandler):
    def get(self):

    if self.request.GET:
        pc1.wage = self.request.GET['wage']
        pc1.hours = self.request.GET['hours']
        pc1.holiday = self.request.GET['holiday']
        pc1.twice = self.request.GET['twice']



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
