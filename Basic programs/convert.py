from pdf2docx import Converter

pdf_file = 'xxx.pdf'
docx_file = 'xxx.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()