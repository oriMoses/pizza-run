from Classes.inventory import Inventory
from Constants.constants import *
from Classes.player import Player

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
        self.inventory.add_item(HOT_PIZZA_ID, "HotPizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(COLD_PIZZA_ID, "ColdPizza", 0, SHOW_ITEM_IN_ROOM)

    def turn_on(self):
        player = Player.getInstance()
        if player.inventory.item_exist(self.vehicleKeyID):
            self.vehicleOn = True
            print("the", self.name, "is on\n")
        else:
            print("You don't have the key to the", self.name)
    
    def is_vehicle_availabe(self):
        player = Player.getInstance()
        
        if self.position != player.position:
            print(self.name, "not nearby")
            return False
        if player.inventory.item_exist(HOT_PIZZA_ID) or player.inventory.item_exist(COLD_PIZZA_ID):
            print("""You can't ride a""", self.name,  "with pizza on your hands (and probably shouldn't try)\n""")
            return False
        if not player.inventory.item_exist(BIKE_KEY_ID):
            print("you don't have the key to the", self.name)
            return False
    
        return True
    
    def can_vehicle_ride(self):
        if not self.vehicleOn:
            print("You have to turn the", self.name, "on")
            return False
        return True
    
    def player_on_vehacle(self):
        return self.playerOnVehicle
    
    def turn_off(self):
        self.vehicleOn = False
        print(self.vehicleName, "is off\n")

    def print_in_room(self):
        pass

    def update_vehicle_location(self, position):
        self.position = position

    def examine(self):
        pass