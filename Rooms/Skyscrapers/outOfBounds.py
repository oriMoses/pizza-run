from Classes.quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *

class OutOfBounds(skyscrapersQuarter):
    def __init__(self, street_name, street_number):
        skyscrapersQuarter.__init__(self, [street_name, street_number]) #Passed code until this line

    def __str__(self):
        return f"Out of bounds"

    def dialog_circle(self, handleChoiceObject, player):
        pass