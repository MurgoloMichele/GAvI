# recupero documenti dalla dir e inserirli in un indice
import os, os.path
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
from os import listdir
from os.path import isfile, join

def get_schema():
    return Schema(path=ID(unique=True, stored=True), content=TEXT)

def get_path():
    return "/home/simone/Documents/UNI/GestioneAvanzataInfo/esercizi"

def get_index_path():
    return "index"

def gather_docs():
    "gather documents into dir and put into an array files"
    files = [f for f in listdir(get_path()) if isfile(join(get_path(), f))]
    return files

def clean_index(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    # Always create the index from scratch
    ix = create_in(dirname, schema=get_schema())
    ix = open_dir(dirname)
    writer = ix.writer()

    # Assume we have a function that gathers the filenames of the
    # documents to be indexed
    for path in gather_docs():
        add_doc(writer, path)

    writer.commit()

def add_doc(writer, path):
    fileobj = open(path, "rb")
    content = fileobj.read()
    fileobj.close()
    writer.add_document(path=unicode(path), content=unicode(content))

# MAIN
clean_index(get_index_path())

# with ix.searcher() as searcher:
#     list(searcher.lexicon("content"))
