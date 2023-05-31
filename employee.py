from attendance import Attendance
from faker import Faker

fake = Faker()


class Employee:
    def __init__(self):
        self.__firstname = fake.first_name()
        self.__lastname = fake.last_name()
        self.__attendances: list[Attendance] = []

        for _ in range(31):
            self.__attendances.append(Attendance())

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
