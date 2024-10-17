from Rooms.pizza_place import PizzaPlace
from Rooms.parking import Parking
from Rooms.none_special_room import NoneSpecialRoom
from Rooms.teen_house import TeenHouse
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
COLD_PIZZA_ID = 1
HOT_PIZZA_ID = 2
COIN_ID = 3

MAX_PIZZA_ON_PLAYER = 5

def init_suburbs():
    global Suburbs
    suburbs_rows, suburbs_cols = (6, 5)
    Suburbs = [[0 for _ in range(suburbs_cols)] for _ in range(suburbs_rows)]

    for i in range(suburbs_cols):
        for j in range(suburbs_rows):
            Suburbs[j][i] = NoneSpecialRoom(j, i)

    for i in range(suburbs_cols):
        for j in range(suburbs_rows):
            if i == 3:
                if j == 3:
                    Suburbs[j][i] = NoneSpecialRoom(j, i)

    Suburbs[3][3] = pizzaPlaceObject
    Suburbs[3][2] = parkingObject
    Suburbs[2][1] = teenHouseObject
    
    ######Debug
    # for i in range(suburbs_cols):
    #     for j in range(suburbs_rows):
    #         print(j, i, Suburbs[j][i])

    
def init():
    global pizzaPlaceObject, parkingObject, player, commonChoiceObject, querters \
            ,teenHouseObject, goNextRoom
    parkingObject = Parking()
    pizzaPlaceObject = PizzaPlace()
    commonChoiceObject = HandleChoices()
    teenHouseObject = TeenHouse()
    player = Player(pizzaPlaceObject.location) # Starting point for player

    init_suburbs()

    goNextRoom = False
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
    