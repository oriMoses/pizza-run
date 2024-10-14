from property_boxes import suburbsBox
from Classes.common_choices import CommonChoices
import Classes.settings as Settings

class PizzaPlace():
    def __init__(self):
        suburbsBox.__init__(self, [3,3])

    def dialog_circle(self, commonChoiceObject):
        while True:
            Settings.player.choice = input("> ").lower()

            if "go" in Settings.player.choice:
                if "north" in Settings.player.choice or "south" in Settings.player.choice \
                                                        or "east" in Settings.player.choice:
                    print("You can't go that way")

                elif "west" in Settings.player.choice:
                    print("The door is locked")

            elif commonChoiceObject.check_player_input():
                pass