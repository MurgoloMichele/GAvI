from whoosh import qparser
from whoosh.analysis import RegexTokenizer
from whoosh.analysis import LowercaseFilter
from whoosh.analysis import StopFilter


def queryCorrection(query, index):

    #f = open('words.txt')
    #words = f.read()
    #word_list = words.split('\n')
    #c1 = ListCorrector(word_list)

    # Parse the user query string
    qp = qparser.QueryParser("content", index.ix.schema)

    analyzer = RegexTokenizer() | LowercaseFilter() | StopFilter()

    # Try correcting the query
    with index.ix.searcher() as s:
        #print(c1.suggest(query, limit=5, maxdist=2))

        for token in analyzer(query):
            q = qp.parse(token.text)
            corrected = s.correct_query(q, token.text)
            if corrected.query != q:
                print("Did you mean:", corrected.string, " instead of ", token.text, "\n")
