'''
Dakota Gillette
10/8/15
DWP
Simple Form
'''


class Page(): #page class
    def __init__(self, page_main): # set instances for class
        self.css = "css/style.css" # grabbing the stylesheet for the page
        self.head = '''<!DOCTYPE HTML>  <!-- initializing the HTML -->
        <html>
            <head>
                <title>Pizza Order Form</title>
            </head>
            <body> '''
            # starting the HTML body
        self.body = '''<form method="GET">
                    <label>Name: </label><input type="text" name="user" />
                    <br><br>
                    <label>Phone Number </label><input type="text" name="phone"/>
                    <br><br>
                    <label>Your Address </label><input type="text" name="address"/>
                    <br><br>
                    <label>Pizza Type: </label><select name="pizzaType">
                    <option value="pepperoni">Pepperoni</option>
                    <option value="cheese">Cheese</option>
                    <option value="hawaiian">Hawaiian</option>
                    <option value="supreme">Supreme</option>
                    </select>
                    <br><br>
                    <label>Select One: </label><input type="radio" name="orderType" value="delivery" checked>Delivery
                    <input type="radio" name="orderType" value="carryout">Carryout
                    <br><br>
                    <textarea name="request" rows="10" cols="30">Leave any special requests in this field</textarea>
                    <br><br>
                    <input type="submit" value="Submit" />'''

        self.close = '''
                </form>
            </body>
        </html>'''

        def print_info(self, x=''): #prints info
            if x=='':
                all = self.head + self.body + self.close # grabs these elements from the HTML
                all = all.format(**locals()) # css is now enabled
                return all # returns the variable, all
            else
                return self.head + x + self.close