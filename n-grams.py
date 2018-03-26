# recupero documenti dalla dir e inserirli in un indice
from whoosh.index import *
from whoosh.fields import *
from whoosh.formats import *
from whoosh.analysis import *


import time
from os import listdir
from os.path import isfile, join, splitext

import xml.sax
from whoosh.qparser import QueryParser

from parse.xmldocument import XMLDocument
from index.index import DocumentIndex
from docretrieve import *
from query_correction import *

query = queryCorrection()
print(query.spellCheck("efectivnes"))
