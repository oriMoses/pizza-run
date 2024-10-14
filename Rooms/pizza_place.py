from suburbsQuarter import suburbsQuarter
from Classes.common_choices import CommonChoices
import Classes.settings as Settings

class PizzaPlace():
    def __init__(self):
        suburbsQuarter.__init__(self, [3,3])
        self.firstArrival = True

    def dialog_circle(self, commonChoiceObject):
        print("Main Pizza Place")

        if self.firstArrival:
            print("It's your basic pizza place, the floor is sticky and the cook is probably 16..\
                  \n\nYou know that place.\n")
            #TODO:        small/medium/massive
            print("You see massive pile of hot pizza and a small note on the counter\nThere's a locked door to the west.")
            self.firstArrival = False

        while True:
            if Settings.goNextRoom:
                break
            Settings.player.choice = input("> ").lower()
            if "look" in Settings.player.choice or "lookaround" in Settings.player.choice:
                print("You see massive pile of hot pizza and a small note on the counter.")

            # elif "go" in Settings.player.choice:
            elif "north" in Settings.player.choice or "south" in Settings.player.choice \
                                                    or "east" in Settings.player.choice:
                print("You can't go that way")

            elif "west" in Settings.player.choice:
                if Settings.player.inventory.item_exist(Settings.KEY_ID):
                    commonChoiceObject.check_player_input()
                    break
                else:
                    print("The door is locked")

            elif commonChoiceObject.check_player_input():
                pass