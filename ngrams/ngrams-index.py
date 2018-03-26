# recupero documenti dalla dir e inserirli in un indice
from whoosh.index import *
from whoosh.fields import *
from whoosh.formats import *
from whoosh.analysis import *

from whoosh.qparser import QueryParser

import time
from os import listdir
from os.path import isfile, join, splitext

# not sure how your schema looks like exactly
schema = Schema(
    ngram=TEXT(stored=True),
    word=TEXT(stored=True))

  

if not os.path.exists("index-index"):
	os.mkdir("index-index")
	ix = create_in("index-index", schema)

	wordlist = []
	f = open("words.txt")
	words = f.read()
	wordlist = words.split('\n')

	writer = ix.writer()

	my_analyzer = StandardAnalyzer() | NgramFilter(minsize=2, maxsize=4)
	for word in wordlist:
		print ('adding', word)
		writer.add_document(word=word, ngram=str(my_analyzer(word)))
	writer.commit()

ix = open_dir("index-index")





origQueryString = "hello"
#words = self.splitQuery(origQueryString) # use tokenizers / analyzers or self implemented
words = [origQueryString]
queryString = origQueryString # would be better to actually create a query
'''
corrector = ix.searcher().corrector("spelling")
for word in words:
	suggestionList = corrector.suggest(word, limit=10)
	print(word)
	for suggestion in suggestionList:
		queryString = queryString + " " + suggestion # would be better to actually create a query  
  '''  


parser = QueryParser("word", ix.schema)
myquery = parser.parse(queryString)

with ix.searcher() as searcher:
	results = searcher.search(myquery)
	print (len(results))

	for r in results:
		print (r)	




































