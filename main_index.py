import xml.sax
from os.path import isfile, join, splitext

from parse.xmldocument import XMLDocument
from index.index import DocumentIndex
from docretrieve import *
from whoosh.qparser import QueryParser


def getfilelist(dir, type):
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


# working dir
dir = "/home/davide/Desktop/00"

# create new index
index = DocumentIndex(getSchema())
index.cleanIndex(dir)

# list of file to parse
files = getfilelist(dir, ".nxml")

# add each file to the index
for f in files:
    doc = parseDocument(join(dir, f))
    index.addDoc(f, doc)
    print(doc.title)


index.open(dir)

searcher = index.ix.searcher()
parser = QueryParser("title", index.ix.schema)
query = parser.parse(u"circulating")
results = searcher.search(query)
for r in results:
    print(r)