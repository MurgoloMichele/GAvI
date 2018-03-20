import npyscreen


class MenuForm(npyscreen.Form):

    def create(self):
        self.name = "Menu"
        self.wgmenu = self.add(npyscreen.MultiLine, values=
            [
                " - Create the index",
                " - Execute custom query",
                " - Perform a benchmark",
                " - Exit"
            ],
            max_height=5
        )

        self.wgbenchmark_type = self.add(npyscreen.SelectOne, values=["Model benchmark", "Query benchmark"])
        self.wgbenchmark_type.hidden = True

    def adjust_widgets(self, *args, **keywords):
        if self.wgmenu.value == 2:
            self.wgbenchmark_type.hidden = False
        else:
            self.wgbenchmark_type.hidden = True

    def afterEditing(self):
        if self.wgmenu.value == 0:
            self.parentApp.setNextForm("INDEX")
        elif self.wgmenu.value == 3:
            self.parentApp.setNextForm(None)