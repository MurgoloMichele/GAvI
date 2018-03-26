from whoosh import qparser
from whoosh.spelling import ListCorrector
from whoosh.spelling import SimpleQueryCorrector

from nltk.util import ngrams

class queryCorrection():
	def __init__(self):
		f = open('words.txt')
		words = f.read()
		self.wordlist = words.split('\n')
		

	def queryCorrection(self, query):
		c1 = ListCorrector(self.wordlist)	
		return c1.suggest(query, limit=100, maxdist=3)



	def jaccard(self, set_1, set_2):
		return len(set_1.intersection(set_2)) / float(len(set_1.union(set_2)))

	def qgrams(self, word, q=3):
		word = '#'*(q-1)+word+'$'*(q-1)
		return ngrams(word,q)

	def spellCheck(self, w,thr=0.5):
		results = None
		score = 0
		englishWords = self.queryCorrection(w)
		if w in englishWords:
			results.append(w)
		else:
			w_qgrams = self.qgrams(w)
			w_qgrams = list(w_qgrams)
			print (w_qgrams)
			for word in englishWords:
				word_qgrams = self.qgrams(word)
				v = self.jaccard(set(w_qgrams),set(word_qgrams))
				if v >= thr and v > score:
					results = word
					score = v
		return (results)

