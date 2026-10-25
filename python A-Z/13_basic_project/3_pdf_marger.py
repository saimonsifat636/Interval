from pypdf import PdfMerger

pdfs = ['pdf1.pdf', 'dummy1.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()