import Classes.settings as Settings
from vehicles.vehicle import Vehicle
from Classes.inventory import Inventory
class Bike(Vehicle):
    def __init__(self, position):
        super().__init__(position, Settings.BIKE_ID, Settings.MAX_PIZZA_ON_BIKE, "Bike")
        self.quarter = "Suburbs"
        
        self.inventory = Inventory()
        self.inventory.add_item(Settings.COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(Settings.HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Bike"
    
    def turn_on(self):
        self.vehicleOn = True

    def turn_off(self):
        self.vehicleOn = False

    def print_in_room(self):
        print("There's a delivery bike in here")

    def examine(self):
        print("An old, bumpy delivery bike. Can get the job done. You can store up to five pizzas on the bike. Faster than walking.")