import xml.sax

from benchmark.xmlquery import XMLQuery
from plot.graphxy import GraphXY
from index.searcher import DocumentSearcher

class QueryBenchmark:


    def __init__(self, query_file, expected_query_res_file,):
        self.query_file = query_file
        self.expected_query_res_file = expected_query_res_file

    def load_query_text(self, query_num):
        # Create the xml parser
        parser = xml.sax.make_parser()
        # Create the document handler
        document = XMLQuery(query_num)
        # Parse the document
        parser.setContentHandler(document)
        parser.setFeature(xml.sax.handler.feature_external_ges, False)
        parser.parse(self.query_file)

        return document.text

    def __load_expected_result(self, query_num):
        documents_expect = []
        # Open file and extract expected relevant document for the query
        with open(self.expected_query_res_file, 'r') as document:
            for line in document:
                arr = (line.replace('\n','\t')).split('\t')
                if(arr[0] == str(query_num)):
                    documents_expect.append(arr[2] + ".nxml")
        return documents_expect

    def rprecisionBenchmark(self, index, model1, model2, r):
        query = self.load_query_text(0)
        expect_res = self.__load_expected_result(0)

    def precisionRecallBenchmark(self, index, model, query_num):
        query = self.load_query_text(query_num)
        expect_res = self.__load_expected_result(query_num)

        searcher = DocumentSearcher(index, model)
        res = searcher.phrasalSearch("content", query)

        ret_doc_set = []
        for i in res:
            ret_doc_set.append(i["path"])

        precision, recall = [], []
        for i in range(1, len(ret_doc_set), 100):
            precision.append(self.__precision(expect_res, ret_doc_set[:i]))
            recall.append(self.__recall(expect_res, ret_doc_set[:i]))

        graph = GraphXY(recall, precision)
        graph.plot()



    def __precision(self, relevant, retrieved):
        precision = len(set(relevant) & set(retrieved)) / len(retrieved)
        return precision

    def __recall(self, relevant, retrieved):
        recall = len(set(relevant) & set(retrieved)) / len(relevant)
        return recall