# recupero documenti dalla dir e inserirli in un indice
import os, os.path, time
from whoosh.index import *
from whoosh.fields import *
from whoosh.formats import *

from os import listdir
from os.path import isfile, join

def getSchema():
    return Schema(
            path=ID(unique=True, stored=True),
            title=TEXT(stored=True),
            authors=KEYWORD(stored=True, commas=True, scorable=True, lowercase=True),
            pubdate=TEXT(stored=True),
            abstract=TEXT(vector=Positions),
            content=TEXT(vector=Positions)
            )

def getPath():
    return "/home/simone/Documents/UNI/GestioneAvanzataInfo/esercizi"

def getModTime(pathToFile):
    return time.ctime(os.path.getmtime(pathToFile))

def getCreationTime(pathToFile):
    return time.ctime(os.path.getctime(pathToFile))

def getIndexPath():
    return "index"

def gatherDocs():
    "gather documents into dir and put into an array files"
    files = [f for f in listdir(get_path()) if isfile(join(get_path(), f))]
    return files



