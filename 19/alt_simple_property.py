from datetime import datetime, timedelta

NOW = datetime.now()



class Promo:
    def __init__(self, name, date):
        self.set_date(date)

    ## getter method to get the properties using an object
    def get_date(self):
        return self.expired

    ## setter method to change the value 'a' using an object
    def set_date(self, date):
        print(date)
        print(NOW)
        if date > NOW:
            self.expired = 'False'
        else:
            self.expired = 'True'

    expired = property(get_date, set_date)
