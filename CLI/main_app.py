import  npyscreen
from CLI.menu_form import MenuForm
from CLI.create_index_form import IndexForm



class MainApp(npyscreen.NPSAppManaged):

    def onStart(self):
        self.registerForm("MAIN", MenuForm())
        self.registerForm("INDEX", IndexForm())


