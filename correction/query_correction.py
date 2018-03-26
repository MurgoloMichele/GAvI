from whoosh import qparser
from whoosh.analysis import RegexTokenizer
from whoosh.analysis import LowercaseFilter
from whoosh.analysis import StopFilter


def editDistanceCorrection(query, index):

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
            #print("Did you mean:", corrected.string, " instead of ", token.text, "\n")

    return corrections