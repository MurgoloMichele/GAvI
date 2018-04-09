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

    def afterEditing(self):
        if self.wgmenu.value == 0:
            self.parentApp.setNextForm("INDEX")
        elif self.wgmenu.value == 1:
            self.parentApp.setNextForm("QUERY")
        elif self.wgmenu.value == 2:
            self.parentApp.setNextForm("BENCHMARK")
        elif self.wgmenu.value == 3:
            self.parentApp.setNextForm(None)
