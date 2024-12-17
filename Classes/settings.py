from Items.suburbsNotebook import SuburbsNotebook
from Items.Keys.mainPizzaKey import MainPizzaKey
from Items.Keys.bike_key import BikeKey
from Items.Keys.green_lawn_mower_key import GreenLawnMowerKey
from Items.Shop.hair_dryer import HairDryer
from Items.Shop.backpack import Backpack
from Items.Shop.pizza_locator import PizzaLocator
from Items.Shop.tripper_guide import TripperGuide
from Items.Shop.wrist_watch import WristWatch
from Items.lawn_mower import LawnMower
from Items.shiny_dice import ShinyDice
from Items.box import Box
from vehicles.bike import Bike
from Classes.player import Player
from Classes.handle_choices import HandleChoices
from Classes.color import Colors
from Constants.constants import *

shop_location = [10,10]
mapInstance = None

def init_orders(map):
    global suburbsOrders, mapInstance
    mapInstance = map
    suburbsOrders = [(5, [0,0]),  (3, [1,0]), (5, [2,1]), (3, [4,1]), (1, [5,2]), (2, [0,3]), (1, [1,3]), (1, [2,4]), (1, [4,4])]


def get_orders_for(streetPosition : int, addressPosition : int):
    global mapInstance
    orderAddress = [streetPosition.value, addressPosition.value]
    for order in suburbsOrders:
        if orderAddress == order[1]:
            return order[0]
    return -1

def remove_orderes_for(streetPosition : int, addressPosition : int):
    global suburbsOrders
    suburbsOrders_list = list(suburbsOrders)
    i=0
    orderAddress = [streetPosition.value, addressPosition.value]

    for order in suburbsOrders:
        if orderAddress == order[1]:
            suburbsOrders_list.pop(i)
            suburbsOrders = tuple(suburbsOrders_list)
        i += 1

def print_objects_in_room(self):
    counter = 0
    if print_items_in_room(self) == NO_ITEMS_IN_ROOM:
        counter += 1
    if print_vehicles_in_room(self) == NO_VEHICLES_IN_ROOM:
        counter += 1
    if print_pizza_in_room(self) == NO_PIZZAS_IN_ROOM:
        counter += 1
    if counter == 3:
        print() #note: if room is empty print 1 empty line to currect spacing


def print_items_in_room(self):
    inBox = False
    inShop = False
    itemInRoom = False
    for item in enumerate(itemList):
        if item[1].ID == SUBURBS_NOTEBOOK_ID or item[1].ID == BIKE_KEY_ID:
            if item[1].inBox:
                inBox = True
        elif item[1].ID == HAIR_DRYER_ID or item[1].ID == PIZZA_LOCATOR_ID or item[1].ID == TRIPPER_GUIDE_ID or item[1].ID == WRIST_WATCH_ID or item[1].ID == BACKPACK_ID:
            if item[1].inShop:
                inShop = True
        if inShop == False and inBox == False:
            if self.inventory.item_exist(item[1].ID):
                item[1].print_in_room()
                itemInRoom = True
    
    if itemInRoom:
        return OK
    else:
        return NO_ITEMS_IN_ROOM
                
def print_vehicles_in_room(self):
    player = Player.getInstance()
    vehicleInRoom = False
    for vehicle in enumerate(vehicleList):
        if vehicle[1].position == player.position:
            vehicle[1].print_in_room()
            vehicleInRoom = True

    if vehicleInRoom:
        return OK
    else:
        return NO_VEHICLES_IN_ROOM
    

def print_pizza_in_room(self):
    hotPizzasInRoom = self.inventory.get_amount(HOT_PIZZA_ID)
    coldPizzasInRoom = self.inventory.get_amount(COLD_PIZZA_ID)

    if hotPizzasInRoom != 0:
        print("There are", str(hotPizzasInRoom), "hot pizzas in here")
        return OK
    elif coldPizzasInRoom != 0:
        print("There are", str(coldPizzasInRoom), "hot pizzas in here")
        return OK
    else:
        return NO_PIZZAS_IN_ROOM

def first_arrival(self):
    if self.firstArrival:
        self.print_first_arrival()
        self.firstArrival = False
    else:
        print_objects_in_room(self)


def howMuchPizza(self, player):
    for numberOfPizza in range(0, MAX_PIZZA_ON_PLAYER+1):
        if str(numberOfPizza) in player.choice:
            return numberOfPizza
    return 0
    
def init_items(map):
    global itemList, shopItemList, SuburbsNotebookObject, mainPizzaKeyObject, boxObject, bikeKeyObject, hairDryerObject, backpackObject, greenLawnMowerKeyObject, PizzaLocatorObject, TripperGuideObject, WristWatchObject, LawnMowerObject, ShinyDiceObject

    SuburbsNotebookObject = SuburbsNotebook(map.suburbs.position[3][2].location)
    mainPizzaKeyObject = MainPizzaKey(map.suburbs.position[3][3].location)
    boxObject = Box()
    bikeKeyObject = BikeKey(map)
    hairDryerObject = HairDryer(shop_location)
    backpackObject = Backpack(shop_location)
    greenLawnMowerKeyObject = GreenLawnMowerKey(map)
    PizzaLocatorObject = PizzaLocator(shop_location)
    TripperGuideObject = TripperGuide(shop_location)
    WristWatchObject = WristWatch(shop_location)
    LawnMowerObject = LawnMower(map)
    ShinyDiceObject = ShinyDice(map)

    shopItemList = [PizzaLocatorObject, TripperGuideObject, WristWatchObject, backpackObject, hairDryerObject]
    itemList = [SuburbsNotebookObject, mainPizzaKeyObject, boxObject, bikeKeyObject, hairDryerObject, greenLawnMowerKeyObject, PizzaLocatorObject, TripperGuideObject, WristWatchObject, LawnMowerObject, ShinyDiceObject, backpackObject]

def init_vehicle(map):
    global bikeObject, vehicleList
    bikeObject = Bike(map)

    vehicleList = [bikeObject]


def init(map):
    global colorsObject, handleChoiceObject, goNextRoom
    handleChoiceObject = HandleChoices()
    colorsObject = Colors()
    
    init_orders(map)
    init_items(map)
    init_vehicle(map)

    goNextRoom = False

def get_address(street, street_number):
    address = get_street_name(street)
    address += get_street_number(street_number)
    return address

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
    player = Player.getInstance()
    if player.quarter == "Suburbs":
        if streetPoition < SUBURBS_MIN_STREET_BOUNDARY or \
            streetPoition > SUBURBS_MAX_STREET_BOUNDARY:
            return False

        if streetNumberPosition < SUBURBS_MIN_STREET_NUMBER_BOUNDARY or \
            streetNumberPosition > SUBURBS_MAX_STREET_NUMBER_BOUNDARY:
            return False

        return True
    