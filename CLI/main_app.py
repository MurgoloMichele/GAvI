import  npyscreen
from CLI.menu_form import MenuForm
from CLI.create_index_form import IndexForm
from CLI.exec_query_form import QueryForm
from CLI.benchmark_form import BenchmarkForm


class MainApp(npyscreen.NPSAppManaged):

    def onStart(self):
        self.registerForm("MAIN", MenuForm())
        self.registerForm("INDEX", IndexForm())
        self.registerForm("QUERY", QueryForm())
        self.registerForm("BENCHMARK", BenchmarkForm())


