import Classes.settings as Settings
from vehicles.vehicle import Vehicle
from Classes.inventory import Inventory
from Constants.constants import *

class Bike(Vehicle):
    def __init__(self, map):
        super().__init__(map.suburbs.position[3][2].location, BIKE_ID, MAX_PIZZA_ON_BIKE, "Bike", BIKE_KEY_ID)
        self.quarter = "Suburbs"

    def __str__(self):
        return f"bike"

    def print_in_room(self):
        if not self.player_on_vehacle():
            if Settings.player.position == Settings.bikeObject.position:
                print("There's a delivery bike in here")

    def examine(self):
        print("An old, bumpy delivery bike. Can get the job done. You can store up to five pizzas on the bike. Faster than walking.")