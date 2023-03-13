from docx2pdf import convert
from docx import Document
from PyPDF2 import PdfMerger, PdfReader

def replace_string(input_filename,output_filename,old_text,new_text):
    doc = Document(input_filename)
    for p in doc.paragraphs:
        if old_text in p.text:
            inline = p.runs
            # Loop added to work with runs (strings with same style)
            for i in range(len(inline)):
                if old_text in inline[i].text:
                    text = inline[i].text.replace(old_text, new_text)
                    inline[i].text = text
            print (p.text)

    doc.save(f'data/{output_filename}.docx')
    return 1


def merge_pdfs(files_input:list,output_file:str):
  merger = PdfMerger()
  for file in files_input:
    merger.append(PdfReader(open(file, 'rb')))
  #merger.append(PdfFileReader(open(filename2, 'rb')))

  merger.write(output_file)
#replace_string('/Users/manas/Documents/dev_new/python/pdf-word/Beginners advice.docx','Me','Ghandi')

#convert("data/dest1.docx", "data/output.pdf")

merge_pdfs([f'data/{i}' for i in ['1.pdf','2.pdf','3.pdf']],'data/merged.pdf')