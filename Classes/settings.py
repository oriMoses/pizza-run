from Rooms.pizza_place import PizzaPlace
from Rooms.parking import Parking
from Rooms.none_special_room import NoneSpecialRoom
from Rooms.teen_house import TeenHouse
from Rooms.blue_house import BlueHouse
from Rooms.hippie_house import HippieHouse
from Rooms.gatekeeper import Gatekeeper
from Rooms.mini_market import MiniMarket
from Rooms.green_house import GreenHouse
from Rooms.yellow_house import YellowHouse
from Rooms.pink_house import PinkHouse
from Rooms.bush_garden import BushGarden
from items.suburbsNotebook import SuburbsNotebook
from items.mainPizzaKey import MainPizzaKey
from Classes.player import Player
from Classes.handle_choices import HandleChoices
#constants
STREET = 0
STREET_NUMBER = 1
SUBURBS_MIN_STREET_BOUNDARY = 0
SUBURBS_MAX_STREET_BOUNDARY = 5
SUBURBS_MIN_STREET_NUMBER_BOUNDARY = 0
SUBURBS_MAX_STREET_NUMBER_BOUNDARY = 4

MainPizzaKey_ID = 0
COLD_PIZZA_ID = 1
HOT_PIZZA_ID = 2
COIN_ID = 3
SUBURBS_NOTEBOOK_ID = 4

MAX_PIZZA_ON_PLAYER = 5
AMOOUNT_OF_ORDERS_IN_SUBURBS = 11

def init_orders():
    global suburbsOrders
    suburbsOrders = [(5, bushGardenObject),  (3, hippieHouseObject), (5, teenHouseObject), (3, blueHouseObject), (1, gatekeeperObject), (2, yellowHouseObject), (1, miniMarketObject), (1, pinkHouseObject), (1, greenHouseObject)]

def get_orders_for(object):
    for item in suburbsOrders:
        if object in item:
            return item[0]
    return -1

def remove_orderes_for(object):
    global suburbsOrders
    suburbsOrders_list = list(suburbsOrders)
    i=0
    for item in suburbsOrders:
        if object in item:
            suburbsOrders_list.pop(i)
            
            suburbsOrders = tuple(suburbsOrders_list)
        i += 1

def print_items_in_room(self):
    for item in enumerate(itemList):
        if player.inventory.item_exist(item[1].ID):
            return
        if item[1].position == player.position:
            item[1].print_in_room()

def init_items():
    global itemList, SuburbsNotebookObject, mainPizzaKeyObject
    SuburbsNotebookObject = SuburbsNotebook(parkingObject.location)
    mainPizzaKeyObject = MainPizzaKey(pizzaPlaceObject.location)

    itemList = [SuburbsNotebookObject, mainPizzaKeyObject]

def underline(text):
    print("\u0332".join(text + " "))

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
    Suburbs[4][1] = blueHouseObject
    Suburbs[1][0] = hippieHouseObject
    Suburbs[5][2] = gatekeeperObject
    Suburbs[1][3] = miniMarketObject
    Suburbs[4][4] = greenHouseObject
    Suburbs[0][3] = yellowHouseObject
    Suburbs[2][4] = pinkHouseObject
    Suburbs[0][0] = bushGardenObject

    ######Debug
    # for i in range(suburbs_cols):
    #     for j in range(suburbs_rows):
    #         print(j, i, Suburbs[j][i])

def init():
    global pizzaPlaceObject, parkingObject, player, commonChoiceObject, querters \
            ,teenHouseObject, blueHouseObject, hippieHouseObject, gatekeeperObject, miniMarketObject\
                , greenHouseObject, yellowHouseObject, pinkHouseObject, bushGardenObject, goNextRoom
    parkingObject = Parking()
    pizzaPlaceObject = PizzaPlace()
    commonChoiceObject = HandleChoices()
    teenHouseObject = TeenHouse()
    blueHouseObject = BlueHouse()
    hippieHouseObject = HippieHouse()
    gatekeeperObject = Gatekeeper()
    miniMarketObject = MiniMarket()
    greenHouseObject = GreenHouse()
    yellowHouseObject = YellowHouse()
    pinkHouseObject = PinkHouse()
    bushGardenObject = BushGarden()

    player = Player(pizzaPlaceObject.location) # Starting point for player


    init_suburbs()
    init_orders()
    init_items()

    goNextRoom = False
    querters = {"Suburbs": Suburbs} #, "Skyscrapers", "Shakedown", "Hood", "Square"]

def print_address(street, street_number):
    address = get_street_name(street)
    address += get_street_number(street_number)
    print(address)

def get_street_number(street_number):
    if street_number == 0:
        return "I"
    if street_number == 1:
        return "II"
    if street_number == 2:
        return "III"
    if street_number == 3:
        return "IV"
    if street_number == 4:
        return "V"

def get_street_name(street):
    if street == 0:
        return "Bush St. "
    elif street == 1:
        return "Love St. "
    elif street == 2:
        return "Freedom St. "
    elif street == 3:
        return "First St. "
    elif street == 4:
        return "Tree St. "
    elif street == 5:
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
    