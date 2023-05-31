from employee import Employee
from report import Report
from fpdf import FPDF

pdf = FPDF()


class PDFReport(Report):
    def create_report(self, filename: str):
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

    def __init__(self):
        self.__employees: list[Employee] = []

        for _ in range(5):
            employee = Employee()
            self.__employees.append(employee)
