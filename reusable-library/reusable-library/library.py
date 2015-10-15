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