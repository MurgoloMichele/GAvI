import os, os.path
from whoosh import index

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

from src.docRetrieve import *

class Index():

    def __init__(self):
        self.ix = ""
        self.schema = Schema(path = ID(unique=True), content=TEXT)
        self.writer = ""
        

    def updateDocument(self):
        ix = index.create_in("index")
        writer = ix.writer()
        writer.addDoc(writer, get_path())
        writer.commit()
        
        writer = ix.indexname()
        writer.updateDocument(path=get_path(), getContent())
        writer.commit()


