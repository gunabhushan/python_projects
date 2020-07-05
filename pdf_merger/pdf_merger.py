import PyPDF2
import sys

inputs = sys.argv[1:]

def merger(pdf_list):
	merge = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		merge.append(pdf)
	merge.write('super.pdf')
	print('all done')


merger(inputs)