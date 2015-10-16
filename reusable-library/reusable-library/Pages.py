"""
Dakota Gillette
10/15/15
"""


class FormPage(object):
    def __init__(self):
        # this is the doc title
        self.__title = "Welcome!"
        # this is the css link
        self.css = "css/styles.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Calculate your paycheck</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """
        # begin body content
        self.body = """
        <div class="content">
        <h1>Calculate your paycheck</h1>
        <form method"GET" action="" name="form" onsubmit="return validateForm();">
            <input id="hours" type="number" placeholder="Hours Worked:" name="hours" required/><br>
            <input id="holiday" type="number" placeholder="Holiday Hours:" name="holiday" required/><br>
            <input id ="wage" type="number" placeholder="Hourly Wage:" name="wage" required/><br>
            <h3>Get paid twice a month?<h3>
            <p>Yes:</P><input id="radio" type="radio" name="twice" value="True" />
            <p>No:</P><input id="radio" type="radio" name="twice" value="False" checked="checked" /><br>
            <input id="submit" type="submit" value="Calculate Pay" onclick="validateForm()" />
        </form>    """

        # errors go here
        self.__error = ''
        self.__close = """
        </div>
        <script src="js/main.js"></script>
    </body>
</html>
                     """
    # this is a printout function used to write html to the page.

    def print_out(self):
        all = self.__head + self.body + self.__error + self.__close
        return all


class ResultsPage(object): # this will be the second page, the results page
    def __init__(self):
        self.__title = "Results"
        self.css = "css/styles.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Here's Your Results:</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>

    <body>
        <div class="content">
        """
        # body content
        self.body = "<h3>You're going to be rich! Keep saving!</h3><br>"
        self.__error = ''
        self.__close = """
                <p id="info">Thank you for calculating your wages! Now go make some more money!</p>
        </div>
        <script src="/js/main.js"></script>
    </body>
</html>
        """
    # this is the printout when someone completes the form

    def print_out(self):
        all = self.__head + self.body + self.__error + self.__close
        return all

