import xml.sax
from os.path import isfile, join, splitext

from parse.xmldocument import XMLDocument
from index.index import DocumentIndex
from docretrieve import *
from whoosh.qparser import QueryParser


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
working_dir = "/home/davide/Desktop/benchmark/pmc-00"
file_dir = working_dir + "/00"

# create new index
index = DocumentIndex(getSchema())
index.cleanIndex(working_dir)

# list of file to parse
files = getFileList(file_dir, ".nxml")

# add each file to the index
i = 0
totDocs = len(files)
start = time.time()

index.beginIndexing()
for f in files:
    doc = parseDocument(join(file_dir, f))
    index.addDoc(f, doc)
    i = i + 1
    print(i, "/", totDocs)
index.endIndexing()

end = time.time()
print("Parsed ", totDocs , " docs in ", end - start, "s")


# Try a query
index.open(working_dir)

searcher = index.ix.searcher()
parser = QueryParser("abstract", index.ix.schema)
query = parser.parse(u"regression")
results = searcher.search(query)
for r in results:
    print(r)