import Classes.settings as Settings
import items.notebook as Notebook
class Box():
    def __init__(self):
        self.quarter = "Suburbs"
        self.position = 3,3
        self.notebook = Notebook()
        self.items = notebook, bikeKey

    def print_notebook(self):
        notebookList = list(self.notebook)
        for i, note in enumerate(notebookList):
            print("x", note[0], " ", end='')
            Settings.print_address(note[1].location[0], note[1].location[1])