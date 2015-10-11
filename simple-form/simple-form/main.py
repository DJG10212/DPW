'''
Dakota Gillette
10/8/15
DWP
Simple Form
'''

import webapp2 # use the webapp2 library
from page import * # imports page.py class

class MainHandler(webapp2.RequestHandler):
    def get(self):
		page = Page() # Creates an instance of the imported class page

		#if there is a URL variable then print this
		if self.request.GET:
			message ="Thank you for your order " + " " + self.request.GET["user"] + " Here is your receipt: <br>" + self.request.GET["phone"] +"<br> " + self.request.GET["address"] + " <br>" + self.request.GET["pizzaType"] + "<br> " + self.request.GET["orderType"] + "<br> " + self.request.GET["request"] + ". Thank you for your order."
			self.response.write(page.header + message + page.closer)

		else:
			self.response.write(page.header + page.registration + page.closer)

# never touch this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
