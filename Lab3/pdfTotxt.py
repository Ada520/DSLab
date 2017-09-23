from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt

#converts pdf, returns its text content as a string
def convert(faname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    infile = open(faname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text


# converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\"  # if no pdfDir passed in
    for pdf in os.listdir(pdfDir):  # iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]

        pdfFilename = pdfDir + pdf
        text = convert(pdfFilename)  # get string of text content of pdf
        textFilename = txtDir + pdf + ".txt"
        textFile = open(textFilename, "w")  # make text file
        textFile.write(text)  # write text to text file


pdfDire = "C:/Users/kevjy/Documents/Fall2017/EE379K/Labs/DSLab/Lab3/scrapedPDF/"
txtDir = "C:/Users/kevjy/Documents/Fall2017/EE379K/Labs/DSLab/Lab3/scrapedTXT/"
convertMultiple(pdfDire, txtDir)