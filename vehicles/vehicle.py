from Classes.inventory import Inventory
import Classes.settings as Settings
class Vehicle():
    def __init__(self, position, itemID, max_pizza_in_inventory, vehicleName):
        self.position = position
        self.ID = itemID
        self.max_pizza_in_inventory = max_pizza_in_inventory
        self.vehicleOn = False
        self.vehicleKeyFound = False
        self.name = vehicleName
        self.playerOnVehicle = False

        self.inventory = Inventory()
        self.inventory.add_item(Settings.HOT_PIZZA_ID, "HotPizza", 0)
        self.inventory.add_item(Settings.COLD_PIZZA_ID, "ColdPizza", 0)

    def turn_on(self):
        self.vehicleOn = True
        print("the ", self.vehicleName, " is on")
    
    def is_vehicle_availabe(self):
        if self.vehicleOn:
            if Settings.player.inventory.item_exist(Settings.HOT_PIZZA_ID) or Settings.player.inventory.item_exist(Settings.COLD_PIZZA_ID):
                print("""You can't ride a """, self.name,  " with pizza on your hands (and probably shouldn't try)""")
                return False
            
            else:
                return True
        else:
            print(self.name, " is off")
            return False
    
    def turn_off(self):
        self.vehicleOn = False
        print(self.vehicleName, " is off")

    def print_in_room(self):
        pass

    def update_vehicle_location(self, position):
        self.position = position

    def examine(self):
        pass