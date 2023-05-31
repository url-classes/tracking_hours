from csv_report import CSVReport
from pdf_report import PDFReport

csv_report = CSVReport()
pdf_report = PDFReport()

csv_report.create_report('asistencias.csv')
pdf_report.create_report('asistencias.pdf')
