import os, os.path
from whoosh import index

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

from docRetrieve import *

class Index():

    def __init__(self):
        # Index object
        self.ix = ""

        # The schema specifies the fields of documents in an index
        self.schema = ""

        # Writer object. Creating a writer locks the index for writing
        # so only one thread/process at a time can have a writer open
        self.writer = ""

        # The set of all paths in the index
        self.indexed_paths = ""

        # Time of index
        self.indexed_time = ""

        # Fields of the document
        self.fields = ""

        # Last modification time of the document
        self.mtime = ""

        # Searcher object
        self.searcher = ""

        # The set of all paths to re-index
        self.to_index = ""
        

    # Method to re-index a document
    def updateDocument(self):
        ix = index.create_in("index")
        writer = ix.writer()
        writer.addDoc(writer, getPath())
        writer.commit()
        
        writer = ix.indexname()
        writer.updateDocument(path=getPath(), content=getContent())
        writer.commit()

    # Method to index all the documents from scratch
    def cleanIndex(self, dirname):
        ix = index.create_in(dirname, schema=getSchema())
        writer = ix.writer()
        addDoc(writer, gatherDocs())
        writer.commit()

    def indexMyDocs(self, dirname, clean=False):
        if clean:
            cleanIndex(dirname)
        else:
            incrementalIndex(dirname)

    # Method to update only the documents that have changed
    def incrementalIndex(self, dirname):
        ix = index.open_dir(dirname)

        # The set of all paths in the index
        indexed_paths = set()

        # The set of all paths we need to re-index
        to_index = set()

        with ix.searcher() as searcher:
            writer = ix.writer()

            # Loop opver the stored fields in the index
            for fields in searcher.all_stored_fields():
                indexed_paths = fields[getPath()]
                indexed_paths.add(indexed_path)

                if not os.path.exists(indexed_path):
                    # This file was deleted since it was indexed
                    writer.delete_by_term(getPath(), indexed_path)
                else:
                    # Check if this file was changed since it was indexed
                    indexed_time = fields[getModTime(getPath())]
                    mtime = getModTime(getPath())
                    if mtime > indexed_time:
                        # The file has changed, delete it and add it to the list
                        # of the files to reindex
                        writer.delete_by_term(getPath(), indexed_path)
                        to_index.add(indexed_path)
            

        # Loop over the files in the filesystem
        addDoc(writer, gatherDocs())
        writer.commit()
