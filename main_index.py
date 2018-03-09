import xml.sax
from whoosh.qparser import QueryParser

from parse.xmldocument import XMLDocument
from index.index import DocumentIndex
from docretrieve import *


# Parse a nxml document
def parseDocument(path):
    # Create the xml parser
    doc_parser = xml.sax.make_parser()

    # Create the document handler
    document = XMLDocument()

    # Parse the document
    doc_parser.setContentHandler(document)
    doc_parser.setFeature(xml.sax.handler.feature_external_ges, False)
    doc_parser.parse(path)
    return document

# Create the index
def createIndex(working_dir):
    # create new index
    doc_index = DocumentIndex(getSchema())
    doc_index.cleanIndex(working_dir)

    # Get dir list
    dir_list = os.listdir(working_dir)

    for dir in dir_list:
        # list of file to parse
        file_dir = working_dir + "/" + dir
        files = getFileList(file_dir, ".nxml")

        i = 0
        tot_docs = len(files)
        start = time.time()

        # add each file to the index
        doc_index.beginIndexing()
        for f in files:
            i = i + 1
            print(dir + "/" + f , "  " , i, "/", tot_docs)
            doc = parseDocument(join(file_dir, f))
            doc_index.addDoc(f, doc)

        doc_index.endIndexing()

        # Print stats
        end = time.time()
        print("Parsed ", tot_docs, " docs in ", end - start, "s")

    return doc_index


# working dir
working_dir = "/home/davide/Desktop/benchmark/pmc-00"
doc_index = createIndex(working_dir)

# Try a query
doc_index.openIndex(working_dir)

searcher = doc_index.ix.searcher()
parser = QueryParser("abstract", doc_index.ix.schema)
query = parser.parse(u"regression")
results = searcher.search(query)
for r in results:
    print(r)
