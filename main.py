import PyPDF4 as pdf
import PyPDF2
import glob

def pdfsplit(filename):
    pdfFileObj = open(filename, 'rb')
    pdfReader = pdf.PdfFileReader(pdfFileObj)
    pagereader = PyPDF2.PdfFileReader(filename)
    for i in range(pdfReader.numPages):
        writefilename = chr(i+49) + '.pdf'
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(pagereader.getPage(i))
        with open(writefilename, 'wb') as output_file:
            pdf_writer.write(output_file)
        #print(i)
    return

def getfilenames(): #put the pdf file in the folder where you run this, it'll take care of the rest for you
    fnlist = []
    for file in glob.glob("[A-z][A-z]*.pdf"):
        fnlist.append(file)
        #print(file)
    print("Slicing",fnlist)
    return fnlist

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fnl = getfilenames()
    for a in range(len(fnl)):
        listlabel = (chr(a+97))
        pdfsplit(listlabel,fnl[a])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
