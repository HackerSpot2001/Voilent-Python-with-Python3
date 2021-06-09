#!/usr/bin/python3
from PyPDF2 import PdfFileReader
import sys
def printMetaData(filename):
    pdfFile = PdfFileReader(filename,'rb')
    docInfo = pdfFile.getDocumentInfo()
    print("[*] PDF MetaData for {}".format(str(filename)))
    for  metaItem in docInfo:
        print("[+] {}: {}".format(metaItem,docInfo[metaItem]))
    
    print('\n')


if __name__ == "__main__":
    usage = "Usage: python3 PDF_Forensics.py file_name"
    if  len(sys.argv)!=2:
        print(usage)
        sys.exit()
    
    print("#"*50)
    print("##\t\tPDF Meta Data Extractor\t\t##")
    print("#"*50)
    filename = str(sys.argv[1])
    printMetaData(filename)