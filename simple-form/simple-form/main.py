'''
Dakota Gillette
10/8/15
DWP
'''

import webapp2  # use the webapp2 library


class MainHandler(webapp2.RequestHandler):  # declaring a class
    def get(self): # function that starts everything. Catalyst
        page_head ='''<!DOCTYPE HTML>
<html>
    <head>
        <title>Pizza Order Form</title>
    </head>
    <body>'''

        page_body = '''<form method="GET">
            <label>Name: </label><input type="text" name="user" />
            <label>Phone Number </label><input type="text" name="phone"/>
            <label>Your Address </label><input type="text" name="address"/>
            <input type="submit" value="Submit" />
            <label>Pizza Type: </label><select name="pizzaType">
            <option value="pepperoni">Pepperoni</option>
            <option value="cheese">Cheese</option>
            <option value="hawaiian">Hawaiian</option>
            <option value="supreme">Supreme</option>
            </select>'''

        page_close = '''
        </form>
    </body>
</html>'''

        if self.request.GET:
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
