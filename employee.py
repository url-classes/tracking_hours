from faker import Faker
from datetime import datetime
from dateutil.relativedelta import relativedelta
import csv
from fpdf import FPDF

fake = Faker()
pdf = FPDF()


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

    def __str__(self):
        result = self.fullname + "\n"
        result += "Attendances:\n"
        for attendance in self.__attendances:
            result += str(attendance) + "\n"

        return result

    def create_csv_report(self, filename: str):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Employee", "Attendance"])
            for attendance in self.__attendances:
                writer.writerow([self.fullname, str(attendance)])

    def create_pdf_report(self, filename: str):
        pdf.set_font("helvetica", size=12)
        pdf.add_page()

        with pdf.table() as table:
            row = table.row()
            row.cell("Employee")
            row.cell("Attendance")
            for attendance in self.__attendances:
                row = table.row()
                row.cell(self.fullname)
                row.cell(str(attendance))

        pdf.output(filename)
