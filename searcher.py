import string
from whoosh import qparser
from whoosh.qparser import QueryParser
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.parse import ChartParser
from nltk.tag import pos_tag

class Searcher:

    def __init__(self, indice):
        self.indice = indice
        self.type = "sercher"

    # retrieve documents from a given query
    def search_doc(self, field, query):
        # stemming with nltk
        wordsFiltered = []
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
            if str(word[1]) in ['NOUN','ADJ']:
                words.append(word[0])

        searcher = self.indice.ix.searcher()
        parser = qparser.QueryParser(field, self.indice.ix.schema, group = qparser.OrGroup)
        q = parser.parse(' '.join(words))
        results = self.indice.ix.searcher().search(q, limit=None, terms=True)
        # see results class whoosh
        return results

    def specific_print(self):
        # Was this results object created with terms=True?
        if results.has_matched_terms():
            # What terms matched in the results?
            print(results.matched_terms())

            # What terms matched in each hit?
            for hit in results:
                print(hit.matched_terms())
