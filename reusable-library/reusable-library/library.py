class Paycheck(object):
    def __init__(self):
        # setting some default values
        self.__twice = False
        self.__wage = 0
        self.__hours = 0
        self.__holiday = 0

    # Twice a month getter/setter

    @property
    def twice(self):
        return self.__twice

    @twice.setter
    def twice(self, y):
        self.__twice = y

    # wage getter/setter
    @property
    def wage(self):
        return self.__wage

    @wage.setter
    def wage(self, w):
        self.__wage = w

    # holiday getter/setter
    @property
    def holiday(self):
        return self.__holiday

    @holiday.setter
    def holiday(self, h):
        self.__holiday = h

    # hour getter/setter
    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, h):
        self.__hours = h


class Calculate(object):
    def __init__(self):
        print "calc starting"
        self.__info = []

        # getting the total
    def total_up(selfself, c):
        self.__info.append(c)