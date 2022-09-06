import PyPDF2
pdfFileObj = open('encrypted.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
pdfReader.decrypt('rosebud')