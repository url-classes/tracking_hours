from faker import Faker
from datetime import datetime
from dateutil.relativedelta import relativedelta

fake = Faker()


class Employee:
    def __init__(self):
        self.__firstname = fake.first_name()
        self.__lastname = fake.last_name()
        self.__attendances: list[datetime] = []

        current_date = datetime.today()
        for _ in range(31):
            check_in = fake.date_time_between(start_date=current_date - relativedelta(months=3))
            self.__attendances.append(check_in)

    @property
    def fullname(self):
        return f"{self.__firstname}, {self.__lastname}"

    @property
    def attendances(self):
        return self.__attendances

    def __str__(self):
        result = self.fullname + "\n"
        result += "Attendances:\n"
        for attendance in self.__attendances:
            result += str(attendance) + "\n"

        return result
