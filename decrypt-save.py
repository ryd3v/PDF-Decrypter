from PyPDF2 import PdfFileReader, PdfFileWriter

encrypted_file='secret.pdf'
decrypted_file='decrypted.pdf'
password='12345'
with open(encrypted_file, 'rb') as input_file, open(decrypted_file, 'wb') as output_file:
    reader = PdfFileReader(input_file)
    reader.decrypt(password)

    writer = PdfFileWriter()

    for i in range(reader.getNumPages()):
        writer.addPage(reader.getPage(i))

    writer.write(output_file)    