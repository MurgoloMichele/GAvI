import os, os.path
from whoosh import index

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

from src.docRetrieve import *

class Index():

    def __init__(self):
        self.ix = ""
        self.schema = ""
        self.writer = ""
        

    def updateDocument(self):
        ix = index.create_in("index")
        writer = ix.writer()
        writer.addDoc(writer, get_path())
        writer.commit()
        
        writer = ix.indexname()
        writer.updateDocument(path=get_path(), getContent())
        writer.commit()

    def cleanIndex(dirname)
        ix = index.create_in(dirname, schema=getSchema())
        writer = ix.writer()
        addDoc(writer, gatherDocs())
        writer.commit()

    def indexMyDocs(dirname, clean=False)
        if clean:
            cleanIndex(dirname)
        else:
            incrementalIndex(dirname)

    def incrementalIndex(dirname)
        ix = index.open_dir(dirname)

        # The set of all paths in the index
        indexedPaths = set()

        # The set of all paths we need to re-index
        to_index = set()



