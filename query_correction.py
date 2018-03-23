from whoosh import qparser
from whoosh.spelling import ListCorrector
from whoosh.spelling import SimpleQueryCorrector

def queryCorrection(query, index):

    # Parse the user query string
    qp = qparser.QueryParser("content", index.ix.schema)
    q = qp.parse(query)

    wordlist = []
    f = open('words.txt')
    words = f.read()
    wordlist = words.split('\n')
			

    # Try correcting the query
    with index.ix.searcher() as s:
        c1 = ListCorrector(wordlist)	
        print(c1.suggest(query,limit=5,maxdist=2))

        '''		
        corrected = s.correct_query(q, query)
        print(corrected.query)
        print(corrected.string)
        if corrected.query != q:
        print ("Did you mean:", corrected.string)
        '''
