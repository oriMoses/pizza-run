from Rooms.pizza_place import PizzaPlace
from Rooms.parking import Parking
from Classes.player import Player
from Classes.handle_choices import HandleChoices

#constants
STREET = 0
STREET_NUMBER = 1
SUBURBS_MIN_STREET_BOUNDARY = 0
SUBURBS_MAX_STREET_BOUNDARY = 5
SUBURBS_MIN_STREET_NUMBER_BOUNDARY = 0
SUBURBS_MAX_STREET_NUMBER_BOUNDARY = 4

KEY_ID = 0
PIZZA_ID = 1

MAX_PIZZA_ON_PLAYER = 5

def init():
    global pizzaPlaceObject, parkingObject, player, commonChoiceObject, Suburbs, querters
    parkingObject = Parking()
    pizzaPlaceObject = PizzaPlace()
    player = Player(pizzaPlaceObject.location)
    commonChoiceObject = HandleChoices()

    goNextRoom = False
    Suburbs = [0],[0]
    querters = {"Suburbs": Suburbs} #, "Skyscrapers", "Shakedown", "Hood", "Square"]

def print_address():
    address = get_current_street_name()
    address += get_current_street_number()
    print("\n" + address + "\n")

def get_current_street_number():
    if player.position[STREET_NUMBER] == 0:
        return "I"
    elif player.position[STREET_NUMBER] == 1:
        return "II"
    elif player.position[STREET_NUMBER] == 2:
        return "III"
    elif player.position[STREET_NUMBER] == 3:
        return "IV"
    elif player.position[STREET_NUMBER] == 4:
        return "V"

def get_current_street_name():
    if player.position[STREET] == 0:
        return "Bush St. "
    elif player.position[STREET] == 1:
        return "Love St. "
    elif player.position[STREET] == 2:
        return "Freedom St. "
    elif player.position[STREET] == 3:
        return "First St. "
    elif player.position[STREET] == 4:
        return "Tree St. "
    elif player.position[STREET] == 5:
        return "Duck St. "

def street_in_boundary(streetPoition, streetNumberPosition):
    if player.quarter == "Suburbs":
        if streetPoition < SUBURBS_MIN_STREET_BOUNDARY or \
            streetPoition > SUBURBS_MAX_STREET_BOUNDARY:
            return False

        if streetNumberPosition < SUBURBS_MIN_STREET_NUMBER_BOUNDARY or \
            streetNumberPosition > SUBURBS_MAX_STREET_NUMBER_BOUNDARY:
            return False

        return True
    