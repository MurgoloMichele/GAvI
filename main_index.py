import xml.sax

from parse.xmldocument import XMLDocument
from index.index import DocumentIndex
from docretrieve import *
from searcher import *
from benchmark.querybenchmark import *
from precision_recall import *
from xy_graph import *


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

def countDoc():
    # Get dir list
    dir_list = getDirList(working_dir)
    tot_docs = 0

    for dir in dir_list:
        # list of file to count
        file_dir = working_dir + "/" + dir
        files = getFileList(file_dir, ".nxml")
        tot_docs = tot_docs + len(files)

    return tot_docs

# working dir
working_dir = "/home/simone/Desktop/pmc-00"
#doc_index = createIndex(working_dir)
QUERY_FILE = "/home/simone/Documents/UNI/GestioneAvanzataInfo/progetto/GAvI/query/topics2014.xml"
RES_FILE = "/home/simone/Documents/UNI/GestioneAvanzataInfo/progetto/GAvI/queryres/qrels-treceval-2014.txt"

# Try a query
doc_index = DocumentIndex(getSchema())
doc_index.openIndex(working_dir)

benchmark = QueryBenchmark(QUERY_FILE, 5, RES_FILE, QueryBenchmark.MODEL_COMPARISON_BENCHMARK)
src = Searcher(doc_index)
res = src.search_doc('content', benchmark.query)

print("# documenti analizzati:", countDoc())
print("query posta:", benchmark.query)
print("\n# documenti ritornati:", len(res.docs()))
print("# documenti attesi:", len(benchmark.expect_res))

ret_doc_set = []
for i in res:
    ret_doc_set.append(i["path"])

pr = PrecisionRecall(countDoc())
precision, recall = [] , []
for i in range(1,len(ret_doc_set),100):
    precision.append(pr.precision(benchmark.expect_res, ret_doc_set[:i]))
    recall.append(pr.recall(benchmark.expect_res, ret_doc_set[:i]))

print(precision)
graph = GraphXY(recall, precision)
graph.plot()
