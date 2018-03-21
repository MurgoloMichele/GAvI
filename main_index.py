import xml.sax

from parse.xmldocument import XMLDocument
from index.index import DocumentIndex
from docretrieve import *
from searcher import *
from benchmark.querybenchmark import *


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
    dir_list = getDirList(working_dir)

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
working_dir = "/home/simone/Desktop/pmc-00"
#doc_index = createIndex(working_dir)
QUERY_FILE = "/home/simone/Documents/UNI/GestioneAvanzataInfo/progetto/GAvI/query/topics2015B.xml"
RES_FILE = "/home/simone/Documents/UNI/GestioneAvanzataInfo/progetto/GAvI/queryres/qrels-treceval-2015.txt"

# Try a query
doc_index = DocumentIndex(getSchema())
doc_index.openIndex(working_dir)

benchmark = QueryBenchmark(QUERY_FILE, 6, RES_FILE, QueryBenchmark.MODEL_COMPARISON_BENCHMARK)
src = Searcher(doc_index)
res = src.search_doc('content', benchmark.query)
print(benchmark.query)
for i in res:
    print(i["path"])
print(len(benchmark.expect_res))
