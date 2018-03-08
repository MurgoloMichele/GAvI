import os.path
from whoosh import index
from docretrieve import *


class DocumentIndex():

    def __init__(self, schema):
        # Index object
        self.ix = None

        # The schema specifies the fields of documents in an index
        self.schema = schema

        # Write
        self.writer = None

    # Method to index all the documents from scratch
    def cleanIndex(self, dirname):
        self.ix = index.create_in(dirname, schema=self.schema)

    def open(self, dir):
        self.ix = index.open_dir(dir)

    def beginIndexing(self):
        self.writer = self.ix.writer(procs=4, limitmb=256, multisegment=True)

    def endIndexing(self):
        self.writer.commit(optimize=True)

    def addDoc(self, path, doc):
        self.writer.add_document(
            path=path,
            title=doc.title,
            authors=",".join(doc.authors),
            pubdate=doc.year + " " + doc.month + " " + doc.day,
            abstract=doc.abstract,
            content=doc.body
        )




    # Method to re-index a document
    def updateDocument(self):
        self.ix = index.create_in("index")
        writer = self.ix.writer()
        writer.addDoc(writer, getPath())
        writer.commit()
        
        writer = self.ix.indexname()
        writer.updateDocument(path=getPath(), content=getContent())
        writer.commit(optimize=True)

   

    def indexMyDocs(self, dirname, clean=False):
        if clean:
            cleanIndex(dirname)
        else:
            incrementalIndex(dirname)

    # Method to update only the documents that have changed
    def incrementalIndex(self, dirname):
        self.ix = index.open_dir(dirname)

        # The set of all paths in the index
        indexed_paths = set()

        # The set of all paths we need to re-index
        to_index = set()

        with self.ix.searcher() as searcher:
            writer = self.ix.writer()

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
