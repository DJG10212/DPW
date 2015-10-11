'''
Dakota Gillette
10/8/15
DWP
Simple Form
'''

class Page():
    def __init__(self): # set instances for class
		self.header ='''<!DOCTYPE HTML> <!--initializing the HTML -->
<html>
    <head>
        <title>Pizza Order Form</title>
        <link rel="stylesheet" href="css/main.css" type="text/css" />
    </head>
    <body>
    <header>
		<h1>Please fill out the form to order your pizza</h1>
	</header>
       '''

		self.registration = form = '''
        <form method="GET" action="">
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
                    <input type="submit" value="Submit" />
        </form>'''

		self.closer = '''
    </body>
</html>'''