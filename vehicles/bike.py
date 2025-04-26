import Classes.settings as Settings
from vehicles.vehicle import Vehicle
from Classes.inventory import Inventory
from Constants.constants import *
from Classes.player import Player

class Bike(Vehicle):
    def __init__(self, map):
        super().__init__([3,2], BIKE_ID, MAX_PIZZA_ON_BIKE, "Bike", BIKE_KEY_ID)
        self.quarter = "Suburbs"

    def __str__(self):
        return f"bike"

    def print_in_room(self):
        player = Player.getInstance()
        if not self.player_on_vehacle():
            if player.position == Settings.bikeObject.position:
                print("\nThere's a delivery bike in here")

    def examine(self):
        print("An old, bumpy delivery bike. Can get the job done. You can store up to five pizzas on the bike. Faster than walking.")
            #"You see an old beat up bike with a logo of pesent genfield\nThere's a plastic box on the back, that can store up to 5 pizzas"