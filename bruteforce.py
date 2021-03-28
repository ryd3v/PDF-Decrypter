from PyPDF2 import PdfFileReader, PdfFileWriter

cracked = False

# Loading passwords
with open("dict.txt") as f:
    lines = f.readlines()

# Opening file
with open('secret.pdf', 'rb') as input_file:
    reader = PdfFileReader(input_file)
    for password in lines:
        password = password.replace('\n','')
        try:
            status = reader.decrypt(password)
            if status == 1:
                correct_password ='Correct password: %s' % password
                cracked = True
                break
        except:
                pass
if cracked:
    print(correct_password)
else:
    print("Not cracked")