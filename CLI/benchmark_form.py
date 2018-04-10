import npyscreen
import os
from whoosh import scoring

from benchmark.querybenchmark import QueryBenchmark
from index.index import DocumentIndex
from docretrieve import *


class BenchmarkForm(npyscreen.ActionForm):

    def create(self):
        self.name = "Exec query"
        self.wgworkingdir = self.add(npyscreen.TitleFilename, name="Index dir:", select_dir=True)
        self.wgqueryfile = self.add(npyscreen.TitleFilename, name="Query file:", select_dir=True)
        self.wgexpectedfile = self.add(npyscreen.TitleFilename, name="Result file:", select_dir=True)

        self.wgcorr = self.add(npyscreen.TitleMultiLine, name="Type:", value=0, values=["Precision-Recall", "R-precision"], max_height=3)

        self.wgmodel1 = self.add(npyscreen.TitleCombo, name="Model1:", value=0, values=["BM25", "TF_IDF", "Frequency"], max_height=1)
        self.wgmodel2 = self.add(npyscreen.TitleCombo, name="Model2:", value=0, values=["BM25", "TF_IDF", "Frequency"], max_height=1)
        self.wgqueryid = self.add(npyscreen.TitleCombo, name="Query id:", value=0, values=range(1, 31), max_height=1)
        self.wgrvalue = self.add(npyscreen.TitleText, name="R-value:", value=0, max_height=1)
        self.wgquerytext = self.add(npyscreen.Pager, max_height=5)

        self.wgerror = self.add(npyscreen.TitleFixedText, name="Error:")
        self.wgerror.hidden = True

        self.wgmodel2.hidden = True
        self.wgrvalue.hidden = True
        self.wgqueryid.hidden = False

    def while_editing(self):
        if os.path.isfile(self.wgexpectedfile.value) and os.path.isfile(self.wgqueryfile.value):
            bench = QueryBenchmark(self.wgqueryfile.value, self.wgexpectedfile.value)

            self.wgquerytext.values = self.splitText(
                bench.load_query_text(int(self.wgqueryid.value) + 1),
                self.wgquerytext.width - 1)

        if self.wgcorr.value == 0:
            self.wgmodel2.hidden = True
            self.wgrvalue.hidden = True
            self.wgqueryid.hidden = False
        else:
            self.wgmodel2.hidden = False
            self.wgrvalue.hidden = False
            self.wgqueryid.hidden = True

        self.display(True)

    def on_cancel(self):
        self.parentApp.setNextForm("MAIN")

    def on_ok(self):
        self.wgerror.value = ""

        if not os.path.isfile(self.wgexpectedfile.value) or not os.path.isfile(self.wgqueryfile.value):
            self.wgerror.value = "Invalid query files"
            self.wgerror.hidden = False

        elif os.path.isdir(self.wgworkingdir.value):
            self.wgerror.hidden = True

            doc_index = DocumentIndex(getSchema())
            doc_index.openIndex(self.wgworkingdir.value)

            bench = QueryBenchmark(self.wgqueryfile.value, self.wgexpectedfile.value)

            model1 = scoring.BM25F
            if self.wgmodel1.value == 1:
                model1 = scoring.TF_IDF
            elif self.wgmodel1.value == 2:
                model1 = scoring.Frequency

            model2 = scoring.BM25F
            if self.wgmodel2.value == 1:
                model2 = scoring.TF_IDF
            elif self.wgmodel2.value == 2:
                model2 = scoring.Frequency

            if self.wgcorr.value == 0:
                bench.precisionRecallBenchmark(doc_index, model1, int(self.wgqueryid.value) + 1)
            else:
                bench.rprecisionBenchmark(doc_index, model1, model2, 10)

        else:
            self.wgerror.value = "Not a directory"
            self.wgerror.hidden = False

    def splitText(self, text, n):
        return list(text[i:i+n] for i in range(0, len(text), n))

