import openpyxl, os

wb = openpyxl.Workbook()
sheet = wb.active
counter=1

for filename in os.listdir(r'C:\Users\ivand\PycharmProjects\automate\ch_13\text files'):
    file = open(filename, 'r')
    text = file.read()

    cell = sheet[f'A{counter}']
    cell.value = text
    counter += 1

wb.save('excel.xlsx')