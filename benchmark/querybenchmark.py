import xml.sax

from src.xmlquery import XMLQuery


class QueryBenchmark:

    PRECISION_RECALL_BENCHMARK = 0
    MODEL_COMPARISON_BENCHMARK = 1

    def __init__(self, query_file, query_num, benchmark_type):
        self.query = self.__load_query_text(query_file, query_num)
        self.type = benchmark_type

    def __load_query_text(self, query_file, query_num):
        # Create the xml parser
        parser = xml.sax.make_parser()
        # Create the document handler
        document = XMLQuery()
        # Parse the document
        parser.setContentHandler(document)
        parser.setFeature(xml.sax.handler.feature_external_ges, False)
        parser.parse(query_file)

        return document.text

    def exec(self):
        result = []

        if self.type == QueryBenchmark.MODEL_COMPARISON_BENCHMARK:
            print("MODEL_COMPARISON_BENCHMARK")

        elif self.type == QueryBenchmark.PRECISION_RECALL_BENCHMARK:
            print("PRECISION_RECALL_BENCHMARK")

        return result
