import xml.sax

from benchmark.xmlquery import XMLQuery


class QueryBenchmark:

    PRECISION_RECALL_BENCHMARK = 0
    MODEL_COMPARISON_BENCHMARK = 1

    def __init__(self, query_file, query_num, expected_query_res_file, benchmark_type):
        self.query = self.__load_query_text(query_file, query_num)
        self.expect_res = self.__load_expected_result(expected_query_res_file, query_num)
        self.type = benchmark_type

    def __load_query_text(self, query_file, query_num):
        # Create the xml parser
        parser = xml.sax.make_parser()
        # Create the document handler
        document = XMLQuery(query_num)
        # Parse the document
        parser.setContentHandler(document)
        parser.setFeature(xml.sax.handler.feature_external_ges, False)
        parser.parse(query_file)

        return document.text

    def __load_expected_result(self, expected_query_res_file, query_num):
        documents_expect = []
        # Open file and extract expected relevant document for the query
        with open(expected_query_res_file, 'r') as document:
            for line in document:
                arr = (line.replace('\n','\t')).split('\t')
                if(arr[0] == str(query_num)):
                    documents_expect.append(arr[2] + ".nxml")
        return documents_expect

    def exec(self):
        result = []

        if self.type == QueryBenchmark.MODEL_COMPARISON_BENCHMARK:
            print("MODEL_COMPARISON_BENCHMARK")

        elif self.type == QueryBenchmark.PRECISION_RECALL_BENCHMARK:
            print("PRECISION_RECALL_BENCHMARK")

        return result
