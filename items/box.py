import Classes.settings as Settings
import items.suburbsNotebook as Notebook
import items.bike_key as BikeKey
from Classes.inventory import Inventory
class Box():
    def __init__(self):
        self.quarter = "Suburbs"
        self.position = 3,2
        self.ID = 100

        self.inventory = Inventory()
        self.inventory.add_item(Settings.BIKE_KEY_ID, "bike key", 1)
        self.inventory.add_item(Settings.SUBURBS_NOTEBOOK_ID, "suburbs notebook", 1)

    def open(self):
        print("You see the suburbs notebook and a bike key")