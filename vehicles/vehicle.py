from Classes.inventory import Inventory
from Constants.constants import *
from Classes.player import Player
from Constants.enums import Colors
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
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)

    def turn_on(self):
        player = Player.getInstance()
        if player.inventory.item_exist(self.vehicleKeyID):
            self.vehicleOn = True
            print("the " + Colors.GREEN + self.name + Colors.END + " is on\n")
        else:
            print("You don't have the key to the " + Colors.GREEN + self.name + Colors.END)
    
    def is_vehicle_availabe(self):
        player = Player.getInstance()
        
        if self.position != player.position:
            print(Colors.GREEN + self.name + Colors.END + " not nearby")
            return False
        if player.inventory.item_exist(HOT_PIZZA_ID) or player.inventory.item_exist(COLD_PIZZA_ID):
            print("""You can't ride a """ + Colors.GREEN + self.name + Colors.END + " with pizza on your hands (and probably shouldn't try)\n""")
            return False
        if not player.inventory.item_exist(BIKE_KEY_ID):
            print("you don't have the key to the " + Colors.GREEN + self.name + Colors.END)
            return False
    
        return True
    
    def can_vehicle_ride(self):
        if not self.vehicleOn:
            print("You have to turn the " + Colors.GREEN + self.name + Colors.END + " on")
            return False
        return True
    
    def player_on_vehacle(self):
        return self.playerOnVehicle
    
    def turn_off(self):
        self.vehicleOn = False
        print(Colors.GREEN + self.name + Colors.END + " is off\n")

    def print_in_room(self):
        pass

    def update_vehicle_location(self, position):
        self.position = position

    def examine(self):
        pass
    
    def print_in_room(self):
        player = Player.getInstance()
        if not self.player_on_vehacle():
            if player.position == self.position:
                print("\nThere's a delivery " + Colors.GREEN + self.name + Colors.END + " in here ", end=' ')
                self.inventory.print_pizzas_on(self.inventory, player.player_on_vehacle, Colors.GREEN + self.name + Colors.END)
