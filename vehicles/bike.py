import Classes.settings as Settings
from vehicles.vehicle import Vehicle
from Classes.inventory import Inventory
class Bike(Vehicle):
    def __init__(self):
        super().__init__(Settings.parkingObject.location, Settings.BIKE_ID, Settings.MAX_PIZZA_ON_BIKE, "Bike", Settings.BIKE_KEY_ID)
        self.quarter = "Suburbs"
        #TODO: if off dont move
    def __str__(self):
        return f"Bike"

    def turn_off(self):
        self.vehicleOn = False

    def print_in_room(self):
        if not self.player_on_vehacle():
            if Settings.player.position == Settings.bikeObject.position:
                print("There's a delivery bike in here")

    def examine(self):
        print("An old, bumpy delivery bike. Can get the job done. You can store up to five pizzas on the bike. Faster than walking.")