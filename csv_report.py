from employee import Employee
from report import Report
import csv


class CSVReport(Report):
    def __init__(self):
        self.__employees: list[Employee] = []

        for _ in range(5):
            employee = Employee()
            self.__employees.append(employee)

    def add_employee(self, employee: Employee):
        self.__employees.append(employee)

    def create_report(self, filename: str):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Employee", "Attendance"])
            for employee in self.__employees:
                for attendance in employee.attendances:
                    writer.writerow([employee.fullname, str(attendance)])
