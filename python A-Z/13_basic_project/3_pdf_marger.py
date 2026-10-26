from PyPDF2 import PdfWriter

merger = PdfWriter()

for i in range(0,3):
    pdf=input("please enter the pdf file name: ")
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()