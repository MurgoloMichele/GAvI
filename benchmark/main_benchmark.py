
from src.querybenchmark import QueryBenchmark


benchmark = QueryBenchmark("/home/davide/Desktop/Uni/GAVI/GAvI/query/topics2014.xml", 10, QueryBenchmark.MODEL_COMPARISON_BENCHMARK)
print(benchmark.query)
benchmark.exec()
