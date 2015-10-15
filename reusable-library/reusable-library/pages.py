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
        form method"GET" action="" name="form" onsubmit="return validateForm();">
        <input id="hours" type="number" placeholder="Hours Worked:" name="hours" required/><br>

    </body>
</html>
        """

    def print_out(self):
            all = self.__head + self.body + self.__error + self.__close
            return all
