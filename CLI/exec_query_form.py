import npyscreen
import os.path

from index.index import DocumentIndex
from index.searcher import DocumentSearcher
from docretrieve import *

from whoosh import scoring

class QueryForm(npyscreen.ActionForm):

    def create(self):
        self.name = "Exec query"
        self.wgworkingdir = self.add(npyscreen.TitleFilename, name="Index dir:", select_dir=True)
        self.wgtitle = self.add(npyscreen.TitleText, name="Title:", value="*")
        self.wgbody = self.add(npyscreen.TitleText, name="Content:", value="")
        self.wgautors = self.add(npyscreen.TitleText, name="Authors:", value="*")
        #self.wgmindate = self.add(npyscreen.TitleDateCombo, name="Pub min date:", value="")
        #self.wgmaxdate = self.add(npyscreen.TitleDateCombo, name="Pub max date:", value="")
        self.wgmodel = self.add(npyscreen.TitleCombo, name="Model:", value=0, values=["BM25", "TF_IDF", "Frequency"], max_height=2)

        self.wgerror = self.add(npyscreen.TitleFixedText, name="Error:")
        self.wgerror.hidden = True

        self.wgresults = self.add(npyscreen.Pager, name="Result:", value="")


    def on_cancel(self):
        self.parentApp.setNextForm("MAIN")

    def on_ok(self):
        if os.path.isdir(self.wgworkingdir.value):
            self.wgerror.hidden = True

            index = DocumentIndex(getSchema())
            index.openIndex(self.wgworkingdir.value)

            model = scoring.BM25F
            if self.wgmodel.value == 1:
                model = scoring.TF_IDF
            elif self.wgmodel.value == 2:
                model = scoring.Frequency

            searcher = DocumentSearcher(model)
            results = searcher.multiFieldSearch(index,
               {
                   "title": self.wgtitle.value,
                   "content": self.wgbody.value,
                   "authors": self.wgautors.value,
               }
            )

            self.wgresults.values = []
            res = []
            for r in results:
                res += [r["path"] + " published on " + r["pubdate"].replace(" ", "/")]
                res += self.splitText(r["title"], self.wgresults.width - 1)
                res += [r["authors"][:self.wgresults.width]]
                #res += self.splitText(r["abstract"], self.wgresults.width - 1)
                res += "\n"
            self.wgresults.values = res

        else:
            self.wgerror.value = "Not a directory"
            self.wgerror.hidden = False

    def splitText(self, text, n):
        return list(text[i:i+n] for i in range(0, len(text), n))

