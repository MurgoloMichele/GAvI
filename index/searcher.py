from whoosh.qparser import QueryParser


class DocumentSearcher:
    # retrieve documents from a given query
    def searchDoc(self, index, field, query):
        parser = QueryParser(field, index.ix.schema)
        q = parser.parse(query)
        # with statement so the searcher is automatically closed when you’re done with it

        results = index.ix.searcher().search(q, limit=None, terms=True)

        return results

    def multiFieldSearch(self, index, query_dict):
        min = 0;
        results = []

        for field in query_dict:
            results.append(self.searchDoc(index, field, query_dict[field]))

        for i in range(0, len(results)):
            if len(results[i]) < len(results[min]):
                min = i

        for i in range(0, len(results)):
            results[min].upgrade(results[i])

        return results[min]