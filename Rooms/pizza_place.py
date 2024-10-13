from property_boxes import suburbsBox
from Classes.common_choices import CommonChoices
import Classes.settings as Settings

class PizzaPlace():
    def __init__(self):
        suburbsBox.__init__(self, [3,3])


    def dialog_circle(self, commonChoiceObject):
        while True:
            Settings.player.choice = input("> ").lower()

            if commonChoiceObject.check_player_input():
                pass