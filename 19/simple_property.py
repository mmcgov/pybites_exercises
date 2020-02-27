from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name, expired)
        self.name = name
        self.expired = expired

    def exp_check(self, expired):
        if expired > NOW:
            return 'True'
        else:
            return 'False'

    expired = property(exp_check)

