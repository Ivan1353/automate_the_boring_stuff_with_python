import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet.freeze_panes = 'A2'