class Page(object):
    def __init__(self):
        # this is the doc title
        self.__title = "Welcome!"
        # this is the css link
        self.css = "css/styles.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Enter your information:</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """
        # begin body content
        self.body = """
        <h1>Calculate your paycheck</h1>
        <form method"GET" action="" name="form" onsubmit="return validateForm();">
            <input id="hours" type="number" placeholder="Hours Worked:" name="hours" required/><br>
            <input id="holiday" type="number" placeholder="Holiday Hours:" name="holiday" required/><br>
            <input id ="wage" type="number" placeholder="Hourly Wage:" name="wage" required/><br>
            Get paid twice a month?<br>
            Yes:<input id="radio" type="radio" name="twice" value="True" /><br>
            No:<input id="radio" type="radio" name="twice" value="False" checked="checked" /><br>
            <input id="submit" type="submit" value="Calculate Pay" onclick="validateForm()" />
        </form>    """

        # errors go here
        self.__error= ''
        self.__close="""
        <script src="js/main.js"></script>
    </body>
</html>
                     """
    # this is a printout function used to write html to the page.
    def print_out(self):
            all = self.__head + self.body + self.__error + self.__close
            return all

class ResultsPage(object):
    def __init__(self):
        # results page title
        self.__title = "Results"
        # css for the document
        self.css = "css/styles.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Here are your results:</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>"""
        # begin body content
        self.body = "<h2>Weekly Income</h3><br>"
        self.__error = ''
        self.__close = """
        <script src="js/main.js"></script>
    </body>
</html>"""
        # this is the printout when someone completes the form

        def print_out(self):
            all = self.__head + self.body + self.__error + self.__close
            return all
