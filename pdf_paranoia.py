import PyPDF2, os
c = 1

for filename in os.listdir():
    if filename[-3:] == 'pdf':
        file = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(file, 'rb')
        pdfWriter = PyPDF2.PdfFileWriter()
        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))
        pdfWriter.encrypt(f'password{c}')
        c+=1
        new_file = open(f'encrypted_{filename}', 'wb')
        pdfWriter.write(new_file)
        new_file.close