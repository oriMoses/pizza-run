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
from Rooms.Shakedown.shakedown_none_special_room import ShakedownNoneSpecialRoom
from Rooms.Shakedown.crowd import Crowd
from Rooms.Shakedown.backStage import BackStage
from Rooms.Shakedown.artistPass import ArtistPass
from Rooms.Shakedown.telephonePoll import TelephonePoll
from Rooms.Shakedown.mainStage import MainStage
from Rooms.Shakedown.scissorLift import ScissorLift
from Rooms.Shakedown.pawnShop import PawnShop
from Rooms.Shakedown.pizzaBooth import PizzaBooth
from Rooms.Shakedown.fakeTickets import FakeTickets
from Rooms.Shakedown.pub import Pub
from Rooms.Shakedown.club import Club
from Rooms.Shakedown.bridge import Bridge
from Rooms.Shakedown.block_1 import Block_1
from Rooms.Shakedown.block_2 import Block_2
from Rooms.Shakedown.somewhere import Somewhere
from Rooms.Shakedown.clockTower import ClockTower
from Rooms.Shakedown.infoBooth import InfoBooth
from Rooms.Shakedown.bigSlide import BigSlide
from Rooms.Shakedown.downUnder import DownUnder
from Rooms.Shakedown.gate import Gate
from Rooms.Shakedown.safetyCenter import SafetyCenter
from Rooms.Shakedown.insideSafetyCenter import InsideSafetyCenter
from Rooms.Shakedown.safetyGuy import SafetyGuy

from Constants.enums import Suburbs_Street_Name, Suburbs_Street_Number, Skyscrapers_Street_Name, Skyscrapers_Street_Number,Shakedown_Street_Number, Shakedown_Street_Name

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
            
            self.position = [[SkyscrapersNoneSpecialRoom(street_name, street_number) for street_name in range(streets_name_quantity)] for street_number in range(streets_number_quantity)]

            self.position[0][0] = OutOfBounds(Skyscrapers_Street_Name.CRASH,Skyscrapers_Street_Number.I)
            self.position[0][3] = OutOfBounds(Skyscrapers_Street_Name.CRASH,Skyscrapers_Street_Number.IV)
            self.position[0][4] = OutOfBounds(Skyscrapers_Street_Name.CRASH,Skyscrapers_Street_Number.V)
            self.position[0][5] = OutOfBounds(Skyscrapers_Street_Name.CRASH,Skyscrapers_Street_Number.VI)
            
            self.position[1][0] = OutOfBounds(Skyscrapers_Street_Name.BURN,Skyscrapers_Street_Number.I) #TODO: Create table in loop instead of by hand
            self.position[1][1] = OutOfBounds(Skyscrapers_Street_Name.BURN,Skyscrapers_Street_Number.II)
            self.position[1][3] = OutOfBounds(Skyscrapers_Street_Name.BURN,Skyscrapers_Street_Number.IV)
            self.position[1][4] = OutOfBounds(Skyscrapers_Street_Name.BURN,Skyscrapers_Street_Number.V)
            self.position[1][5] = OutOfBounds(Skyscrapers_Street_Name.BURN,Skyscrapers_Street_Number.VI)
            
            self.position[3][0] = OutOfBounds(Skyscrapers_Street_Name.SECOND,Skyscrapers_Street_Number.I)
            self.position[3][1] = OutOfBounds(Skyscrapers_Street_Name.SECOND,Skyscrapers_Street_Number.II)
            self.position[3][3] = OutOfBounds(Skyscrapers_Street_Name.SECOND,Skyscrapers_Street_Number.IV)
            self.position[3][5] = OutOfBounds(Skyscrapers_Street_Name.SECOND,Skyscrapers_Street_Number.VI)
            
            self.position[4][0] = OutOfBounds(Skyscrapers_Street_Name.LUCK,Skyscrapers_Street_Number.I)
            self.position[4][1] = OutOfBounds(Skyscrapers_Street_Name.LUCK,Skyscrapers_Street_Number.II)
            
            self.position[2][0] = TradeCenter()
            self.position[0][1] = Bank()
            self.position[2][1] = MainRoad(Skyscrapers_Street_Name.MAIN,Skyscrapers_Street_Number.II)
            self.position[2][3] = MainRoad(Skyscrapers_Street_Name.MAIN,Skyscrapers_Street_Number.IV)
            self.position[2][4] = MainRoad(Skyscrapers_Street_Name.MAIN,Skyscrapers_Street_Number.V)
            self.position[2][5] = MainRoad(Skyscrapers_Street_Name.MAIN,Skyscrapers_Street_Number.VI)
            
            self.position[0][2] = SideRoad(Skyscrapers_Street_Name.CRASH,Skyscrapers_Street_Number.III)
            self.position[1][2] = SideRoad(Skyscrapers_Street_Name.BURN,Skyscrapers_Street_Number.III)
            self.position[1][6] = SideRoad(Skyscrapers_Street_Name.BURN,Skyscrapers_Street_Number.VII)
            self.position[3][6] = SideRoad(Skyscrapers_Street_Name.SECOND,Skyscrapers_Street_Number.VII)
            self.position[4][6] = SideRoad(Skyscrapers_Street_Name.SECOND,Skyscrapers_Street_Number.VII)
            
            self.position[2][2] = CrossRoads()
            self.position[3][2] = GoldenGate()
            self.position[4][2] = CasinoParking()

            self.position[4][3] = CasinoLobby()

            self.position[3][4] = CasinoRoof()
            self.position[4][4] = Elevator()

            self.position[4][5] = CasinoMainHall()
            self.position[0][6] = RoadConstruction()
            self.position[2][6] = EndOfMainRoad()

    class ShakedownConstructor():
        def __init__(self):
            streets_name_quantity, streets_number_quantity = (7, 7)
            
            self.position = [[ShakedownNoneSpecialRoom(street_number, street_name) for street_number in range(streets_number_quantity)] for street_name in range(streets_name_quantity)]

            self.position[0][2] = Crowd(Shakedown_Street_Name.DUCK,Shakedown_Street_Number.III)
            self.position[0][3] = BackStage()
            self.position[0][4] = ArtistPass()
            self.position[0][6] = TelephonePoll()

            self.position[1][2] = Crowd(Shakedown_Street_Name.PLATE,Shakedown_Street_Number.III)
            self.position[1][3] = MainStage()
            self.position[1][4] = Crowd(Shakedown_Street_Name.PLATE,Shakedown_Street_Number.V)

            self.position[2][2] = Crowd(Shakedown_Street_Name.SPOON,Shakedown_Street_Number.III)
            self.position[2][3] = Crowd(Shakedown_Street_Name.SPOON,Shakedown_Street_Number.IV)
            self.position[2][4] = Crowd(Shakedown_Street_Name.SPOON,Shakedown_Street_Number.V)
            self.position[2][5] = ScissorLift()

            self.position[3][0] = PawnShop()
            self.position[3][1] = PizzaBooth()
            self.position[3][2] = FakeTickets()
            self.position[3][3] = Gate()
            self.position[3][4] = Pub()
            self.position[3][5] = Club()
            self.position[3][6] = Bridge()
            
            self.position[5][1] = Block_1()
            self.position[5][2] = Block_2()
            self.position[5][3] = ClockTower()

            self.position[6][0] = InfoBooth()
            self.position[6][1] = Somewhere(Shakedown_Street_Name.LATE,Shakedown_Street_Number.II)
            self.position[6][2] = Somewhere(Shakedown_Street_Name.LATE,Shakedown_Street_Number.III)
            self.position[6][3] = BigSlide()
            self.position[6][4] = DownUnder()
            self.position[6][5] = SafetyCenter()
            self.position[6][6] = InsideSafetyCenter()
            self.position[5][6] = SafetyGuy()
                    
    class HoodConstructor():
        def __init__(self):
            pass


    getInstance = mapHelper()

    def __init__(self):
        self.suburbs = self.SuburbsConstructor()
        self.skyscrapers = self.SkyscrapersConstructor()
        self.shakedown = self.ShakedownConstructor()
