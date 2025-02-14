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
from Rooms.Suburbs.none_special_room import NoneSpecialRoom
from Rooms.Skyscrapers.tradeCenter import TradeCenter
from Rooms.Skyscrapers.bank import Bank
from Rooms.Skyscrapers.mainRoad import MainRoad
from Rooms.Skyscrapers.sideRoad import SideRoad
from Rooms.Skyscrapers.crossRoads import CrossRoads
from Rooms.Skyscrapers.goldenGate import GoldenGate
from Rooms.Skyscrapers.casinoParking import CasinoParking
from Rooms.Skyscrapers.casinoLobby import CasinoLobby
from Rooms.Skyscrapers.casinoRoot import CasinoRoot
from Rooms.Skyscrapers.elevator import Elevator
from Rooms.Skyscrapers.casinoMainHall import CasinoMainHall
from Rooms.Skyscrapers.roadConstruction import RoadConstruction
from Rooms.Skyscrapers.sideRoad_6_1 import SideRoad_6_1
from Rooms.Skyscrapers.endOfMainRoad import EndOfMainRoad
from Rooms.Skyscrapers.sideRoad_6_3 import SideRoad_6_3
from Rooms.Skyscrapers.sideRoad_6_4 import SideRoad_6_4
from Constants.enums import Street_Number, Street_Name

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
            suburbs_rows, suburbs_cols = (6, 5)
            self.position = [[0 for _ in range(suburbs_cols)] for _ in range(suburbs_rows)]

            for i in range(suburbs_cols):
                for j in range(suburbs_rows):
                    self.position[j][i] = NoneSpecialRoom(j, i)

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
            skyscrapers_rows, skyscrapers_cols = (7, 5)
            self.position = [[0 for _ in range(skyscrapers_cols)] for _ in range(skyscrapers_rows)]

            for i in range(skyscrapers_cols):
                for j in range(skyscrapers_rows):
                    self.position[j][i] = NoneSpecialRoom(j, i)

            self.position[0][2] = TradeCenter()
            self.position[1][0] = Bank()
            self.position[1][2] = MainRoad(Street_Name.MAIN,Street_Number.II)
            self.position[2][0] = SideRoad()
            self.position[2][2] = CrossRoads()
            self.position[2][3] = GoldenGate()
            self.position[2][4] = CasinoParking()
            self.position[3][2] = MainRoad(Street_Name.MAIN,Street_Number.IV)
            self.position[3][4] = CasinoLobby()
            self.position[4][2] = MainRoad(Street_Name.MAIN,Street_Number.V)
            self.position[4][3] = CasinoRoot()
            self.position[4][4] = Elevator()
            self.position[5][2] = MainRoad(Street_Name.MAIN,Street_Number.VI)
            self.position[5][4] = CasinoMainHall()
            self.position[6][0] = RoadConstruction()
            self.position[6][1] = SideRoad_6_1()
            self.position[6][2] = EndOfMainRoad()
            self.position[6][3] = SideRoad_6_3()
            self.position[6][4] = SideRoad_6_4()
            
    class ShakedownConstructor():
        def __init__(self):
            pass


    getInstance = mapHelper()

    def __init__(self):
        self.suburbs = self.SuburbsConstructor()
        self.skyscrapers = self.SkyscrapersConstructor()
        self.shakedown = self.ShakedownConstructor()
