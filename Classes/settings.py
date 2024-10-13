from Rooms.pizza_place import PizzaPlace
from Rooms.parking import Parking
from Classes.player import Player
from Classes.common_choices import CommonChoices

def init():
    global pizzaPlaceObject, parkingObject, player, commonChoiceObject, Suburbs, querters
    parkingObject = Parking()
    pizzaPlaceObject = PizzaPlace()
    player = Player(parkingObject.location)
    commonChoiceObject = CommonChoices()


    Suburbs = [0],[0]
    querters = {"Suburbs": Suburbs} #, "Skyscrapers", "Shakedown", "Hood", "Square"]