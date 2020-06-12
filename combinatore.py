<<<<<<< HEAD
import PyPDF2
import os
from PyPDF2 import PdfFileMerger, PdfFileReader

#you should insert here the path to the directory where the pdf are
os.chdir("C:\\Python")



#depending on how many file you have, if you want to open them and check you can put the name of the file and rb
pdf1File=open("A.pdf", "rb")
pdf2File=open("B.pdf", "rb")

#the file will be then readed and saved in variables
reader1= PyPDF2.PdfFileReader(pdf1File)
reader2= PyPDF2.PdfFileReader(pdf2File)


writer= PyPDF2.PdfFileWriter()

#extracting the text

for pageNum in range(reader1.numPages):
    print(reader1.getPage(pageNum).extractText())
#
#
for pageNum in range(reader2.numPages):
    print(reader2.getPage(pageNum).extractText())
#
#
#
#
for page in range(reader1.numPages):
    page=reader1.getPage(pageNum)
    writer.addPage(page)
#
for page in range(reader2.numPages):
    page=reader2.getPage(pageNum)
    writer.addPage(page)



#the final file!
outputfile= open("mixitall.pdf", "wb")
writer.write(outputfile)

outputfile.close
=======
import PyPDF2
import os
from PyPDF2 import PdfFileMerger, PdfFileReader

#you should insert here the path to the directory where the pdf are
os.chdir("C:\\Python")



#depending on how many file you have, if you want to open them and check you can put the name of the file and rb
pdf1File=open("A.pdf", "rb")
pdf2File=open("B.pdf", "rb")

#the file will be then readed and saved in variables
reader1= PyPDF2.PdfFileReader(pdf1File)
reader2= PyPDF2.PdfFileReader(pdf2File)


writer= PyPDF2.PdfFileWriter()

#extracting the text

for pageNum in range(reader1.numPages):
    print(reader1.getPage(pageNum).extractText())
#
#
for pageNum in range(reader2.numPages):
    print(reader2.getPage(pageNum).extractText())
#
#
#
#
for page in range(reader1.numPages):
    page=reader1.getPage(pageNum)
    writer.addPage(page)
#
for page in range(reader2.numPages):
    page=reader2.getPage(pageNum)
    writer.addPage(page)



#the final file!
outputfile= open("mixitall.pdf", "wb")
writer.write(outputfile)

outputfile.close
>>>>>>> 02017cafa9e5d0e9b2c4a4b6d1bb180fc0b808bf
