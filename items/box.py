import Classes.settings as Settings
import Items.suburbsNotebook as Notebook
import Items.Keys.bike_key as BikeKey
from Classes.inventory import Inventory
from Constants.constants import *
from Constants.enums import Colors, quarter
class Box():
    def __init__(self):
        self.quarter = quarter.SUBURBS
        self.position = 3,2
        self.ID = 100
        self.box_open = False

        self.inventory = Inventory()
        self.inventory.add_item(BIKE_KEY_ID, "bike key", 1, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(SUBURBS_NOTEBOOK_ID, "suburbs notebook", 1, SHOW_ITEM_IN_ROOM)

    def print_items_inside(self):
        if self.inventory.item_exist(SUBURBS_NOTEBOOK_ID) and self.inventory.item_exist(BIKE_KEY_ID):
            print("You see the ", end='')
            print(Colors.GREEN + "suburbs notebook " + Colors.END, end='')
            print("and a ", end='')
            print(Colors.GREEN + "bike key" + Colors.END+"\n")
            
        elif self.inventory.item_exist(SUBURBS_NOTEBOOK_ID):
            print("You see the " + Colors.GREEN + "suburbs notebook\n" + Colors.END)
            
        elif self.inventory.item_exist(BIKE_KEY_ID):
            print("You see " + Colors.GREEN + "bike key\n" + Colors.END)
        else:
            print("(box is empty)\n")
            
    def open(self):
        print(Colors.BROWN + "(box opened)\n" + Colors.END)
        self.print_items_inside()
