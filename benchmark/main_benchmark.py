
from querybenchmark import QueryBenchmark

QUERY_FILE = "/home/simone/Documents/UNI/GestioneAvanzataInfo/progetto/GAvI/query/topics2014.xml"
RES_FILE = "/home/simone/Documents/UNI/GestioneAvanzataInfo/progetto/GAvI/queryres/qrels-treceval-2014.txt"

benchmark = QueryBenchmark(QUERY_FILE, 10, RES_FILE, QueryBenchmark.MODEL_COMPARISON_BENCHMARK)
print(benchmark.query)
print(len(benchmark.expect_res))
benchmark.exec()
