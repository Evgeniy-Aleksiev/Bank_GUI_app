import json
import os


class CreditCalculator:
    DB_FOLDER_NAME = 'db'
    BANK_DB = 'bank_db.txt'

    def __init__(self, user, amount, period, interest_percent, max_amount, max_period, credit_type):
        self.user = user
        self.amount = amount
        self.period = period
        self.interest_percent = interest_percent
        self.max_amount = max_amount
        self.max_period = max_period
        self.credit_type = credit_type

    def interest(self):
        if self.credit_type == 'consumer credit' or self.credit_type == 'housing loan':
            if self.amount > self.max_amount:
                return f'Amount can not be bigger than {self.max_amount}'
        else:
            if self.amount < 20:
                return f'Amount can not be les than 20'

        if self.period > self.max_period:
            return f'The maximum period is {self.max_period}'

        interest_for_period = (((self.amount * self.interest_percent) / 12)
                               + (self.amount / self.period)) * self.period
        return f"{interest_for_period:.2f}"

    def get_credit(self):
        not_in_db = True
        with open(os.path.join(self.DB_FOLDER_NAME, self.BANK_DB), 'r+') as file:
            users = file.readlines()
            file.seek(0)

            for user in users:
                user_as_dict = json.loads(user)
                if user_as_dict.get('username') == self.user:
                    user_as_dict['credits'][self.credit_type] = self.interest()
                    not_in_db = False
                file.write(json.dumps(user_as_dict))
                file.write('\n')

            if not_in_db:
                user_credit = {'username': self.user,
                               'credits': {'consumer credit': 0,
                                           'housing loan': 0,
                                           'saving account': 0}}
                user_credit['credits'][self.credit_type] = self.interest()
                file.write(json.dumps(user_credit))
                file.write('\n')


class ConsumerCredit(CreditCalculator):
    _INTEREST_PERCENT = 0.0695
    _MAX_AMOUNT = 75000
    _MAX_PERIOD = 120
    _CREDIT_TYPE = 'consumer credit'

    def __init__(self, user, amount, period):
        super().__init__(user, amount, period, self._INTEREST_PERCENT,
                         self._MAX_AMOUNT, self._MAX_PERIOD, self._CREDIT_TYPE)


class HousingLoanPage(CreditCalculator):
    _INTEREST_PERCENT = 0.0267
    _MAX_AMOUNT = 500000
    _MAX_PERIOD = 420
    _CREDIT_TYPE = 'housing loan'

    def __init__(self, user, amount, period):
        super().__init__(user, amount, period, self._INTEREST_PERCENT,
                         self._MAX_AMOUNT, self._MAX_PERIOD, self._CREDIT_TYPE)


class SavingAccountPage(CreditCalculator):
    _INTEREST_PERCENT = 0.0015
    _MAX_AMOUNT = 500000
    _MAX_PERIOD = 120
    _CREDIT_TYPE = 'saving account'

    def __init__(self, user, amount, period):
        super().__init__(user, amount, period, self._INTEREST_PERCENT,
                         self._MAX_AMOUNT, self._MAX_PERIOD, self._CREDIT_TYPE)
