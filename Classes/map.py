from Rooms.Suburbs.parking import Parking
from Rooms.Suburbs.blue_house import BlueHouse
from Rooms.Suburbs.pink_house import PinkHouse
from Rooms.Suburbs.teen_house import TeenHouse
from Rooms.Suburbs.gatekeeper import Gatekeeper
from Rooms.Suburbs.bush_garden import BushGarden
from Rooms.Suburbs.green_house import GreenHouse
from Rooms.Suburbs.mini_market import MiniMarket
from Rooms.Suburbs.pizza_place import PizzaPlace
from Rooms.Suburbs.hippie_house import HippieHouse
from Rooms.Suburbs.yellow_house import YellowHouse
from Rooms.Suburbs.suburbs_none_special_room import SuburbsNoneSpecialRoom
from Rooms.Skyscrapers.skyscrapers_none_special_room import SkyscrapersNoneSpecialRoom
from Rooms.Shakedown.shakedown_none_special_room import ShakedownNoneSpecialRoom
from Rooms.Skyscrapers.tradeCenter import TradeCenter
from Rooms.Skyscrapers.bank import Bank
from Rooms.Skyscrapers.mainRoad import MainRoad
from Rooms.Skyscrapers.sideRoad import SideRoad
from Rooms.Skyscrapers.crossRoads import CrossRoads
from Rooms.Skyscrapers.goldenGate import GoldenGate
from Rooms.Skyscrapers.casinoParking import CasinoParking
from Rooms.Skyscrapers.casinoLobby import CasinoLobby
from Rooms.Skyscrapers.casinoRoof import CasinoRoof
from Rooms.Skyscrapers.elevator import Elevator
from Rooms.Skyscrapers.casinoMainHall import CasinoMainHall
from Rooms.Skyscrapers.roadConstruction import RoadConstruction
from Rooms.Skyscrapers.sideRoad import SideRoad
from Rooms.Skyscrapers.outOfBounds import OutOfBounds
from Rooms.Skyscrapers.endOfMainRoad import EndOfMainRoad
from Constants.enums import Suburbs_Street_Name, Suburbs_Street_Number, Skyscrapers_Street_Name, Skyscrapers_Street_Number,Shakedown_Street_Number

class Map():
    instance = None
    suburbs = None
    skyscrapers = None
    shakedown = None

    class mapHelper(): #this class make sure Map is a singletone and instantiate only once
        def __call__( self, *args, **kw ):
            if Map.instance is None:
                mapObject = Map()
                Map.instance = mapObject
            
            return Map.instance
        
    class SuburbsConstructor():
        def __init__(self):
            streets_name_quantity, streets_number_quantity = (6, 5)
            
            self.position = [[SuburbsNoneSpecialRoom(street_number, street_name) for street_number in range(streets_number_quantity)] for street_name in range(streets_name_quantity)]
            
            self.position[3][3] = PizzaPlace()
            self.position[3][2] = Parking()
            self.position[2][1] = TeenHouse()
            self.position[4][1] = BlueHouse()
            self.position[1][0] = HippieHouse()
            self.position[5][2] = Gatekeeper()
            self.position[1][3] = MiniMarket()
            self.position[4][4] = GreenHouse()
            self.position[0][3] = YellowHouse()
            self.position[2][4] = PinkHouse()
            self.position[0][0] = BushGarden()
            
    class SkyscrapersConstructor():
        def __init__(self):
            streets_name_quantity, streets_number_quantity = (7, 5)
            
            self.position = [[SkyscrapersNoneSpecialRoom(street_number, street_name) for street_number in range(streets_number_quantity)] for street_name in range(streets_name_quantity)]

            self.position[0][0] = OutOfBounds(Skyscrapers_Street_Name.CRASH,Skyscrapers_Street_Number.I)
            self.position[0][1] = OutOfBounds(Skyscrapers_Street_Name.BURN,Skyscrapers_Street_Number.I) #TODO: Create table in loop instead of by hand
            self.position[1][1] = OutOfBounds(Skyscrapers_Street_Name.BURN,Skyscrapers_Street_Number.II)
            self.position[0][3] = OutOfBounds(Skyscrapers_Street_Name.SECOND,Skyscrapers_Street_Number.I)
            self.position[1][3] = OutOfBounds(Skyscrapers_Street_Name.SECOND,Skyscrapers_Street_Number.II)
            self.position[0][4] = OutOfBounds(Skyscrapers_Street_Name.LUCK,Skyscrapers_Street_Number.I)
            self.position[1][4] = OutOfBounds(Skyscrapers_Street_Name.BURN,Skyscrapers_Street_Number.II)
            self.position[3][0] = OutOfBounds(Skyscrapers_Street_Name.BURN,Skyscrapers_Street_Number.IV)
            self.position[3][1] = OutOfBounds(Skyscrapers_Street_Name.BURN,Skyscrapers_Street_Number.IV)
            
            self.position[3][3] = OutOfBounds(Skyscrapers_Street_Name.BURN,Skyscrapers_Street_Number.VI)
            self.position[4][0] = OutOfBounds(Skyscrapers_Street_Name.BURN,Skyscrapers_Street_Number.V)
            self.position[4][1] = OutOfBounds(Skyscrapers_Street_Name.SECOND,Skyscrapers_Street_Number.V)
            self.position[5][0] = OutOfBounds(Skyscrapers_Street_Name.SECOND,Skyscrapers_Street_Number.V)
            self.position[5][1] = OutOfBounds(Skyscrapers_Street_Name.SECOND,Skyscrapers_Street_Number.V)
            self.position[5][3] = OutOfBounds(Skyscrapers_Street_Name.SECOND,Skyscrapers_Street_Number.V)
            self.position[0][2] = TradeCenter()
            self.position[1][0] = Bank()
            self.position[1][2] = MainRoad(Skyscrapers_Street_Name.MAIN,Skyscrapers_Street_Number.II)
            self.position[3][2] = MainRoad(Skyscrapers_Street_Name.MAIN,Skyscrapers_Street_Number.IV)
            self.position[4][2] = MainRoad(Skyscrapers_Street_Name.MAIN,Skyscrapers_Street_Number.V)
            self.position[5][2] = MainRoad(Skyscrapers_Street_Name.MAIN,Skyscrapers_Street_Number.VI)
            
            self.position[2][1] = SideRoad(Skyscrapers_Street_Name.CRASH,Skyscrapers_Street_Number.III)
            self.position[6][1] = SideRoad(Skyscrapers_Street_Name.BURN,Skyscrapers_Street_Number.VII)
            self.position[6][3] = SideRoad(Skyscrapers_Street_Name.BURN,Skyscrapers_Street_Number.VII)
            self.position[6][4] = SideRoad(Skyscrapers_Street_Name.BURN,Skyscrapers_Street_Number.VII)
            
            self.position[2][2] = CrossRoads()
            self.position[2][3] = GoldenGate()
            self.position[2][4] = CasinoParking()

            self.position[3][4] = CasinoLobby()

            self.position[4][3] = CasinoRoof()
            self.position[4][4] = Elevator()

            self.position[5][4] = CasinoMainHall()
            self.position[6][0] = RoadConstruction()
            self.position[6][2] = EndOfMainRoad()

    class ShakedownConstructor():
        def __init__(self):
            streets_name_quantity, streets_number_quantity = (7, 7)
            
            self.position = [[ShakedownNoneSpecialRoom(street_number, street_name) for street_number in range(streets_number_quantity)] for street_name in range(streets_name_quantity)]
        
    class HoodConstructor():
        def __init__(self):
            pass


    getInstance = mapHelper()

    def __init__(self):
        self.suburbs = self.SuburbsConstructor()
        self.skyscrapers = self.SkyscrapersConstructor()
        self.shakedown = self.ShakedownConstructor()
