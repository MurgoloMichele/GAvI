from whoosh import qparser

def queryCorrection(query)
    
    # Parse the user query string
    qp = qparser.QueryParser(query, myindex.schema)
    q = qp.parse(qstring)

    # Try correcting the query
    with ix.searcher() as s:
        corrected = s.correctQuery(q, qstring)
        print(corrected)
        print(corrected.query)
        if corrected.query != q:
            for mistyped_word in mistyped_words:
                print corrector.suggest(mistyped_word, limit=3, maxdist=2)
