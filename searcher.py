from whoosh.qparser import QueryParser

# retrieve documents from a given query
def search_doc(indice, field, query):
    searcher = indice.ix.searcher()
    parser = QueryParser(field, indice.ix.schema)
    q = parser.parse(query)
    print(q)
    # with statement so the searcher is automatically closed when you’re done with it
    with indice.ix.searcher() as s:
        results = searcher.search(q, limit=None, terms=True)

    # print results
    for r in results:
        print(r)

def specific_print():
    # Was this results object created with terms=True?
    if results.has_matched_terms():
        # What terms matched in the results?
        print(results.matched_terms())

        # What terms matched in each hit?
        for hit in results:
            print(hit.matched_terms())
