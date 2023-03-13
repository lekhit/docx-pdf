from docx2pdf import convert
from docx import Document
def replace_string(filename,old_text,new_text):
    doc = Document(filename)
    for p in doc.paragraphs:
        if old_text in p.text:
            inline = p.runs
            # Loop added to work with runs (strings with same style)
            for i in range(len(inline)):
                if old_text in inline[i].text:
                    text = inline[i].text.replace(old_text, new_text)
                    inline[i].text = text
            print (p.text)

    doc.save('data/dest1.docx')
    return 1
#replace_string('/Users/manas/Documents/dev_new/python/pdf-word/Beginners advice.docx','Me','Ghandi')




convert("data/dest1.docx", "data/output.pdf")