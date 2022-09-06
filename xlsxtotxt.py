import openpyxl

wb = openpyxl.load_workbook(r'C:\Users\ivand\PycharmProjects\automate\ch_13\text files\excel.xlsx')
ws = wb.active
count=1

for row in ws['A']:
   text = row.value

   file = open(f'new_file{count}.txt', 'w')
   file.write(text)

   count+=1