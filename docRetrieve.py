# recupero documenti dalla dir e inserirli in un indice
import os, os.path
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
from os import listdir
from os.path import isfile, join

def getSchema():
    return Schema(path=ID(unique=True, stored=True), content=TEXT)

def getPath():
    return "/home/simone/Documents/UNI/GestioneAvanzataInfo/esercizi"

def getIndexPath():
    return "index"

def gatherDocs():
    "gather documents into dir and put into an array files"
    files = [f for f in listdir(get_path()) if isfile(join(get_path(), f))]
    return files


def addDoc(writer, path):
    fileobj = open(path, "rb")
    content = fileobj.read()
    fileobj.close()
    writer.add_document(path=unicode(path), content=unicode(content))
