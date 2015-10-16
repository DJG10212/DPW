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
    def total_up(self, c):
        self.__info.append(c)
        __holiday_hours = int(c.holiday) * 1.5
        __holiday_pay = __holiday_hours * int(c.wage)
        total = int(c.wage) * int(c.hours) + __holiday_pay
        print c.twice
        # if they get paid twice a month, divide by 2
        if c.twice == "True":
            print "Pay check twice a month"
            total = total / 2
        else:
            print "Pay check once a month"
        return total

        # this will sum up everything once we get the total
    def summary_text(self, c):
            total = self.total_up(c)
            print total
            print Paycheck.wage
            # returns the info
            return "<h3>Paycheck: $" + str(total) +"</h3>"



