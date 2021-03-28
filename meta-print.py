from PyPDF2 import PdfFileReader, PdfFileWriter

# Opening file
with open('decrypted.pdf', 'rb') as input_file:
    reader = PdfFileReader(input_file)
    print reader.getDocumentInfo()