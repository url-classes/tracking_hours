import csv
from fpdf import FPDF

from employee import Employee

pdf = FPDF()


class Report:
    def __init__(self):
        self.__employees: list[Employee] = []

        for _ in range(5):
            employee = Employee()
            self.__employees.append(employee)

    def create_csv_report(self, filename: str):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Employee", "Attendance"])
            for employee in self.__employees:
                for attendance in employee.attendances:
                    writer.writerow([employee.fullname, str(attendance)])

    def create_pdf_report(self, filename: str):
        pdf.set_font("helvetica", size=12)
        pdf.add_page()

        with pdf.table() as table:
            row = table.row()
            row.cell("Employee")
            row.cell("Attendance")
            for employee in self.__employees:
                for attendance in employee.attendances:
                    row = table.row()
                    row.cell(employee.fullname)
                    row.cell(str(attendance))

        pdf.output(filename)
