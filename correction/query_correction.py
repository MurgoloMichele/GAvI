from whoosh import qparser
from whoosh.analysis import RegexTokenizer
from whoosh.analysis import LowercaseFilter
from whoosh.analysis import StopFilter

from whoosh import qparser
from whoosh.spelling import ListCorrector

from nltk.util import ngrams

from enchant import DictWithPWL
from enchant.checker import SpellChecker


class QueryCorrection:

    def __init__(self):
        en_dict = self.__load_dict__("en_dict.txt")
        custom_dict = self.__load_dict__("context_dict.txt")

        self.dict = en_dict + custom_dict
        self.list_corrector = ListCorrector(self.dict)
        self.spell_checker = SpellChecker(DictWithPWL("en_US", "context_dict.txt"))

    def __load_dict__(self, name):
        f = open(name)
        words = f.read()
        return words.split('\n')

    def getSuggestions(self, query):
        return self.dict#self.list_corrector.suggest(query, limit=100, maxdist=3)

    def jaccard(self, set_1, set_2):
        return len(set_1.intersection(set_2)) / float(len(set_1.union(set_2)))

    def qgrams(self, word, q=3):
        word = '#' * (q - 1) + word + '$' * (q - 1)
        return ngrams(word, q)

    def ngramsMatcher(self, w, thr=0.2):
        results = None
        score = 0
        englishWords = self.getSuggestions(w)
        if w in englishWords:
            results = w
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

    def contextCorrection(self, query):
        self.spell_checker.set_text(query)

        corrections = []
        for err in self.spell_checker:
            sug = err.suggest()[0]
            corrections.append((err.word, sug))

        return corrections

    def ngramsCorrection(self, query):
        analyzer = RegexTokenizer() | LowercaseFilter() | StopFilter()

        # Try correcting the query
        corrections = []
        for token in analyzer(query):
            corrected = self.ngramsMatcher(token.text)
            if corrected is not None and corrected != token.text:
                corrections.append((token.text, corrected))

        return corrections

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
