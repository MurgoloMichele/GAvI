from whoosh.qparser import QueryParser

# retrieve documents from a given query
def search_doc(query):
    searcher = doc_index.ix.searcher()
    parser = QueryParser("content", doc_index.ix.schema)
    q = parser.parse(query)

    # with statement so the searcher is automatically closed when you’re done with it
    with doc_index.ix.searcher() as s:
        results = searcher.search(q, limit=None, terms=True)

    print_results()

# print all results
def print_results():
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
