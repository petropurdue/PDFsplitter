import PyPDF4 as pdf
import PyPDF2
import glob

#Optional improvements that could be made to this program:
#None! Everything finished!

def two_digit_hex_to_three_digit_integer(hex): #Credit to lmiguelvargasf on stackoverflow for this function
    return str(int(hex, 16)).zfill(3)

def pdfsplit(listlbl, filename): #this is where the splitting actually happens
    #Initializations
    pdfFileObj = open(filename, 'rb')
    pdfReader = pdf.PdfFileReader(pdfFileObj)
    pagereader = PyPDF2.PdfFileReader(filename)

    #Page splitting
    for i in range(pdfReader.numPages):
        writei = two_digit_hex_to_three_digit_integer(hex(i))
        writefilename = listlbl + writei + '.pdf'    #write as a001.pdf, a2.pdf, b1.pdf, b2.pdf, etc
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(pagereader.getPage(i))
        with open(writefilename, 'wb') as output_file:
            pdf_writer.write(output_file)
        #print(i)
    return

def getfilenames(): #put the pdf file in the folder where you run this, it'll take care of the rest for you. You can name it whatever non-integer you want.
    fnlist = []
    for file in glob.glob("[A-z][A-z]*.pdf"): #get all the pdf files that are not outputs from this program and split them
        fnlist.append(file)
        #print(file)
    print("Slicing",fnlist)
    return fnlist

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fnl = getfilenames()
    if fnl != []:
        for a in range(len(fnl)):
            listlabel = (chr(a+97))
            pdfsplit(listlabel,fnl[a])
        print("PDF split successfully!")
    else:
        print("No files received!")