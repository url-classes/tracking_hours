from report import Report

print('Hello world')
report = Report()
report.create_csv_report('asistencias.csv')
report.create_pdf_report('asistencias.pdf')
