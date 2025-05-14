import Classes.settings as Settings
from vehicles.vehicle import Vehicle
from Classes.inventory import Inventory
from Constants.constants import *
from Classes.player import Player
from Constants.enums import Colors
class Bike(Vehicle):
    def __init__(self, map):
        super().__init__([3,2], BIKE_ID, MAX_PIZZA_ON_BIKE, "Delivery Bike", BIKE_KEY_ID)
        self.quarter = "Suburbs"

    def __str__(self):
        return f"Delivery Bike"
    
    def examine(self):
        player = Player.getInstance()
        print('''You see an old beat up ''' + Colors.GREEN + "Bike" + Colors.END + ''' with the logo of "PESENT GENFIELD"\nThere's a plastic box on the back, that can store up to 5 pizzas''')
        if self.inventory.inventory_empty():
            print("\nNo pizza in " + Colors.GREEN + "Bike" + Colors.END)
        else:
            self.inventory.print_pizzas_on(self.inventory, player.player_on_vehacle, Colors.GREEN + "Bike" + Colors.END)