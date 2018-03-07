import xml.sax
from os import listdir
from os.path import isfile, join, splitext

from xmldocument import XMLDocument


def getFileList(dir, type):
    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f)) and splitext(f)[1] == type]

    return onlyfiles


def parseDocument(path):
    # Create the xml parser
    parser = xml.sax.make_parser()
    # Create the document handler
    document = XMLDocument()
    # Parse the document
    parser.setContentHandler(document)
    parser.setFeature(xml.sax.handler.feature_external_ges, False)
    parser.parse(path)

    return document


dir = "/home/davide/Desktop/benchmark/pmc-00/00"
files = getFileList(dir, ".nxml")
print("File to analyze: ", len(files))
input("Premi un tasto per iniziare")
for f in files:
    print(f)
    doc = parseDocument(join(dir, f))
    print(doc.title)
    print(doc.authors)
    print(doc.date)
    print()
