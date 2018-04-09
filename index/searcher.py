import string
from whoosh.qparser import QueryParser
from whoosh import scoring, qparser

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tag import pos_tag


class DocumentSearcher:
    def __init__(self, index, model=scoring.BM25F):
        self.model = model
        self.index = index

    # retrieve documents from a given query
    def phrasalSearch(self, field, query):
        # stemming with nltk
        words = []
        stopWords = set(stopwords.words('english'))
        stemmer = PorterStemmer()

        wordsFiltered = word_tokenize(query)
        # removing punctuation
        wordsFiltered = [word for word in wordsFiltered if word not in string.punctuation]
        # removing stopWords
        wordsFiltered = [word for word in wordsFiltered if word not in stopWords]
        # stemming phase
        wordsFiltered = [stemmer.stem(word) for word in wordsFiltered]
        # adding POS
        wordsFiltered = pos_tag(wordsFiltered, tagset='universal')
        # keep only NOUN and ADJ
        for word in wordsFiltered:
            if str(word[1]) in ['NOUN', 'ADJ']:
                words.append(word[0])

        parser = QueryParser(field, self.index.ix.schema, group=qparser.OrGroup)
        q = parser.parse(' '.join(words))

        results = self.index.ix.searcher(weighting=self.model).search(q, limit=None, terms=True)

        return results

    def keywordSearch(self, field, query):

        parser = QueryParser(field, self.index.ix.schema, group=qparser.OrGroup)
        q = parser.parse(query)

        results = self.index.ix.searcher(weighting=self.model).search(q, limit=None, terms=True)

        return results

    def multiFieldSearch(self, query_dict):
        min_index = 0
        results = []

        for field in query_dict:
            results.append(self.keywordSearch(field, query_dict[field]))

        for i in range(0, len(results)):
            if len(results[i]) < len(results[min_index]):
                min_index = i

        for i in range(0, len(results)):
            results[min_index].upgrade(results[i])

        return results[min_index]