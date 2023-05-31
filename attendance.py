from datetime import datetime
from dateutil.relativedelta import relativedelta
from faker import Faker

fake = Faker()


class Attendance:
    def __init__(self):
        current_date = datetime.today()
        self.__check_in = fake.date_time_between(start_date=current_date - relativedelta(months=3))

    def __str__(self):
        return str(self.__check_in)
