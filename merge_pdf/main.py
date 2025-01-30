from pathlib import Path
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

ROOT_FOLDER = Path(__file__).parent
PDF_FOLDER = ROOT_FOLDER/'pdfs'
MERGED_PDF_FOLDER = ROOT_FOLDER/'merged pdfs'


file = [

    PDF_1 = PDF_FOLDER/'pdf1.pdf'
    PDF_2 = PDF_FOLDER/'pdf2.pdf'

]

merger = PdfMerger()
for file in files:
    merger.append(file)

merger.write(MERGED_PDF_FOLDER/ 'MERGED.pdf')
merger.close()
