page_head ='''<!DOCTYPE HTML>
<html>
    <head>
        <title>Pizza Order Form</title>
    </head>
    <body>'''

        page_body = '''<form method="GET">
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

        page_close = '''
        </form>
    </body>
</html>'''