

import webapp2
from pages import Page, ResultsPage


class MainHandler(webapp2.RequestHandler):
    def get(self):
    # if a GET request is sent then get the right values and show results page
    if self.request.GET:
        pc1.wage = self.request.GET['wage']
        pc1.hours = self.request.GET['hours']
        pc1.holiday = self.request.GET['holiday']
        pc1.twice = self.request.GET['twice']
        p = ResultsPage()
        p.body += cal.summary_text(pc1)
        # if not, keep up the form
    else:
        p = FormPage()

    # writes to the page
    self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
