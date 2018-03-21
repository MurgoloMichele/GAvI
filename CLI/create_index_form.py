import npyscreen
import os.path
import xml.sax

from parse.xmldocument import XMLDocument
from index.index import DocumentIndex
from docretrieve import *


class IndexForm(npyscreen.ActionForm):

    def create(self):
        self.name = "Creating index"
        self.wgworkingdir = self.add(npyscreen.TitleFilename, name="Working dir:", select_dir=True)

        self.wgerror = self.add(npyscreen.TitleFixedText, name="Error:")
        self.wgerror.hidden = True

        self.nextrely += 1

        self.wgindex = self.add(npyscreen.TitleFixedText, name="Indexing:")
        self.wgprogress = self.add(npyscreen.TitleSliderPercent, name="Progress:")
        self.wgprogress.value = 0

    def on_ok(self):
        if os.path.isdir(self.wgworkingdir.value):
            self.wgerror.hidden = True
            self.wgprogress.hidden = False;

            self.createIndex(self.wgworkingdir.value)

            self.wgworkingdir.value = ""
            self.wgprogress.value = 0
            self.wgindex.value = ""
            self.parentApp.setNextForm("MAIN")
        else:
            self.wgerror.value = "Not a directory"
            self.wgerror.hidden = False

    def on_cancel(self):
        self.wgworkingdir.value = ""
        self.parentApp.setNextForm("MAIN")

    # Parse a nxml document
    def parseDocument(self, path):
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
    def createIndex(self, working_dir):
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

            # add each file to the index
            doc_index.beginIndexing()
            for f in files:
                i = i + 1
                doc = self.parseDocument(join(file_dir, f))
                doc_index.addDoc(f, doc)

                # Print stats
                self.wgindex.value = dir + "/" + f
                self.wgprogress.value = i / tot_docs * 100
                self.display()
                self.refresh()

            # Print stats
            self.wgindex.value = "Saving index file..."
            self.display()
            self.refresh()

            doc_index.endIndexing()

