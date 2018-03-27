from whoosh import qparser
from whoosh.analysis import RegexTokenizer
from whoosh.analysis import LowercaseFilter
from whoosh.analysis import StopFilter

from whoosh import qparser
from whoosh.spelling import ListCorrector

from nltk.util import ngrams


class QueryCorrection:

    def __init__(self):
        f = open('en_dict.txt')
        words = f.read()
        self.en_dict = words.split('\n')
        self.list_corrector = ListCorrector(self.en_dict)

    def getSuggestions(self, query):
        return self.list_corrector.suggest(query, limit=100, maxdist=3)

    def jaccard(self, set_1, set_2):
        return len(set_1.intersection(set_2)) / float(len(set_1.union(set_2)))

    def qgrams(self, word, q=3):
        word = '#' * (q - 1) + word + '$' * (q - 1)
        return ngrams(word, q)

    def ngramsCorrection(self, w, thr=0.5):
        results = None
        score = 0
        englishWords = self.getSuggestions(w)
        if w in englishWords:
            results.append(w)
        else:
            w_qgrams = self.qgrams(w)
            w_qgrams = list(w_qgrams)
            for word in englishWords:
                word_qgrams = self.qgrams(word)
                v = self.jaccard(set(w_qgrams), set(word_qgrams))
                if v >= thr and v > score:
                    results = word
                    score = v
        return results

    def editDistanceCorrection(self, query, index):

        # Parse the user query string
        qp = qparser.QueryParser("content", index.ix.schema)

        analyzer = RegexTokenizer() | LowercaseFilter() | StopFilter()

        # Try correcting the query
        s = index.ix.searcher()
        corrections = []
        for token in analyzer(query):
            q = qp.parse(token.text)
            corrected = s.correct_query(q, token.text)
            if corrected.query != q:
                corrections.append((token.text, corrected.string))

        return corrections