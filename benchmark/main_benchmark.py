
from querybenchmark import QueryBenchmark


QUERY_FILE = "/home/davide/Desktop/Uni/GAVI/GAvI/query/topics2014.xml"
RES_FILE = "/home/davide/Desktop/Uni/GAVI/GAvI/queryres/qrels-treceval-2014.txt"

benchmark = QueryBenchmark(QUERY_FILE, 1, RES_FILE, QueryBenchmark.MODEL_COMPARISON_BENCHMARK)
print(benchmark.query)
print(len(benchmark.expect_res))
benchmark.exec()
