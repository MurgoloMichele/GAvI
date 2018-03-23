from whoosh.qparser import QueryParser
from whoosh import scoring


class DocumentSearcher:
    def __init__(self, model=scoring.BM25F):
        self.model = model

    # retrieve documents from a given query
    def searchDoc(self, index, field, query):
        parser = QueryParser(field, index.ix.schema)
        q = parser.parse(query)

        results = index.ix.searcher(weighting=self.model).search(q, limit=None, terms=True)

        return results

    def multiFieldSearch(self, index, query_dict):
        min = 0
        results = []

        for field in query_dict:
            results.append(self.searchDoc(index, field, query_dict[field]))

        for i in range(0, len(results)):
            if len(results[i]) < len(results[min]):
                min = i

        for i in range(0, len(results)):
            results[min].upgrade(results[i])

        return results[min]