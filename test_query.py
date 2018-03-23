import xml.sax
from whoosh.qparser import QueryParser

from parse.xmldocument import XMLDocument
from index.index import DocumentIndex
from docretrieve import *
from query_correction import *
from index.index import *

doc_index = DocumentIndex(getSchema())
doc_index.openIndex("/home/cthulhu/Scaricati/pmc-10")

searcher = doc_index.ix.searcher()
parser = QueryParser("content", doc_index.ix.schema)
query = queryCorrection(u"mammograpy", doc_index)
'''print(query)

results = searcher.search(query)
for r in results:
    print(r)
'''
