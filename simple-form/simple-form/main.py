'''
Dakota Gillette
10/8/15
DWP
Simple Form
'''

import webapp2  # use the webapp2 library
from page import Page # imports the page class from page.py


class MainHandler(webapp2.RequestHandler):  # declaring a class
    def get(self): # function that starts everything. Catalyst


        if self.request.GET: #this brings the variables to the page
            page = Page(self)
            
            user = self.request.GET['user']
            email = self.request.GET['email']
            self.response.write(page_head + user + ' ' + email + page_body + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #PRINT
        # code goes here


# never touch this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
