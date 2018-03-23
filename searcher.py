from whoosh.qparser import QueryParser
from whoosh import qparser

class Searcher:

    def __init__(self, indice):
        self.indice = indice
        self.type = "sercher"

    # retrieve documents from a given query
    def search_doc(self, field, query):
        searcher = self.indice.ix.searcher()
        parser = qparser.QueryParser(field, self.indice.ix.schema, group = qparser.OrGroup)
        q = parser.parse(query)
        # print the query
        # print(q)
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
