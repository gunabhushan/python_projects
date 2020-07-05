import PyPDF2

templet = PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('water.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range(templet.getNumPages()):
	page = templet.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

	with open('watermarked_output.pdf','wb') as file:
		output.write(file)