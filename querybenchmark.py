import xml.sax


class QueryBenchmark():

    PRECISION_RECALL_BENCHMARK = 0
    MODEL_COMPARISON_BENCHMARK = 1

   def __init__(self, queryFile, queryNum, benchmarkType):
       self.queryFile = queryFile;
       self.queryNum = queryNum;