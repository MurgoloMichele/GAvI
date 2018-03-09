from whoosh import index

class DocumentIndex:

    def __init__(self, schema):
        # Index object
        self.ix = None

        # The schema specifies the fields of documents in an index
        self.schema = schema

        # Write
        self.writer = None

    # Create a new index
    def cleanIndex(self, dirname):
        self.ix = index.create_in(dirname, schema=self.schema)

    # Open an existing index
    def openIndex(self, dir):
        self.ix = index.open_dir(dir)

    # Create a writer object
    def beginIndexing(self):
        self.writer = self.ix.writer(procs=4, limitmb=256, multisegment=True)

    # Commit the writer
    def endIndexing(self):
        self.writer.commit(optimize=True)

    # Add a new doc
    def addDoc(self, path, doc):
        self.writer.add_document(
            path=path,
            title=doc.title,
            authors=",".join(doc.authors),
            pubdate=doc.year + " " + doc.month + " " + doc.day,
            abstract=doc.abstract,
            content=doc.body
        )
