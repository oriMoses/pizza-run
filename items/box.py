import Classes.settings as Settings
import Items.suburbsNotebook as Notebook
import Items.Keys.bike_key as BikeKey
from Classes.inventory import Inventory
from Constants.constants import *

class Box():
    def __init__(self):
        self.quarter = "Suburbs"
        self.position = 3,2
        self.ID = 100

        self.inventory = Inventory()
        self.inventory.add_item(BIKE_KEY_ID, "bike key", 1)
        self.inventory.add_item(SUBURBS_NOTEBOOK_ID, "suburbs notebook", 1)

    def open(self):
        if self.inventory.item_exist(SUBURBS_NOTEBOOK_ID) and self.inventory.item_exist(BIKE_KEY_ID):
            print("You see the suburbs notebook and a bike key")
        elif self.inventory.item_exist(SUBURBS_NOTEBOOK_ID):
            print("You see the suburbs notebook")
        elif self.inventory.item_exist(BIKE_KEY_ID):
            print("You see bike key")
        