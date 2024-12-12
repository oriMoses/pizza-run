from Classes.inventory import Inventory
import Classes.settings as Settings
from Constants.constants import *

class Vehicle():
    def __init__(self, position, itemID, max_pizza_in_inventory, vehicleName, vehicleKeyID):
        self.position = position
        self.ID = itemID
        self.max_pizza_in_inventory = max_pizza_in_inventory
        self.vehicleOn = False
        self.vehicleKeyFound = False
        self.name = vehicleName
        self.playerOnVehicle = False
        self.vehicleKeyID = vehicleKeyID

        self.inventory = Inventory()
        self.inventory.add_item(HOT_PIZZA_ID, "HotPizza", 0)
        self.inventory.add_item(COLD_PIZZA_ID, "ColdPizza", 0)

    def turn_on(self):
        if Settings.player.inventory.item_exist(self.vehicleKeyID):
            self.vehicleOn = True
            print("the", self.name, "is on")
        else:
            print("You don't have the key to the", self.name)
    
    def is_vehicle_availabe(self):
        if self.position != Settings.player.position:
            print(self.name, "not nearby")
            return False
        if Settings.player.inventory.item_exist(Settings.HOT_PIZZA_ID) or Settings.player.inventory.item_exist(Settings.COLD_PIZZA_ID):
            print("""You can't ride a""", self.name,  "with pizza on your hands (and probably shouldn't try)""")
            return False
        if not Settings.player.inventory.item_exist(Settings.BIKE_KEY_ID):
            print(self.name, "you don't have the key to the ", self.name)
            return False
    
        return True

    def player_on_vehacle(self):
        return self.playerOnVehicle
    
    def turn_off(self):
        self.vehicleOn = False
        print(self.vehicleName, "is off")

    def print_in_room(self):
        pass

    def update_vehicle_location(self, position):
        self.position = position

    def examine(self):
        pass