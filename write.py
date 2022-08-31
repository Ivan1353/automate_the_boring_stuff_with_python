import openpyxl
wb = openpyxl.Workbook()
wb.sheetnames
sheet = wb.active
sheet.title
sheet.title = 'Spam Bacon Eggs Sheet'
sheet['A1'] = 'Hello, world!'
wb.save('my_workbook.xlsx')

