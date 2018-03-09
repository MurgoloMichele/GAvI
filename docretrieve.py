# recupero documenti dalla dir e inserirli in un indice
from whoosh.index import *
from whoosh.fields import *
from whoosh.formats import *
from whoosh.analysis import *


import time
from os import listdir
from os.path import isfile, join, splitext


def getSchema():
    return Schema(
            path=ID(unique=True, stored=True),
            title=TEXT(analyzer=StemmingAnalyzer()),
            authors=TEXT(stored=True),
            pubdate=DATETIME(stored=True),
            abstract=TEXT(vector=Positions, analyzer=StemmingAnalyzer()),
            content=TEXT(vector=Positions, analyzer=StemmingAnalyzer())
            )

def getModTime(path):
    return time.ctime(os.path.getmtime(path))

def getCreationTime(path):
    return time.ctime(os.path.getctime(path))

def getFileList(dir, type):
    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f)) and splitext(f)[1] == type]
    return onlyfiles

def getDirList(dir):
    onlydir = [f for f in listdir(dir) if not isfile(join(dir, f))]
    return onlydir
