from employee import Employee

print('Hello world')
employee1 = Employee()
employee1.create_csv_report('asistencia.csv')
employee1.create_pdf_report('asistencia.pdf')
