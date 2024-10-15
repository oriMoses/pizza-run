from suburbsQuarter import suburbsQuarter
import Classes.settings as Settings

class Parking(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [3,2])
        self.firstArrival = True

    def dialog_circle(self, commonChoiceObject):
        print("Teen house")
        if self.firstArrival:
            print("You are in the pizza parking lot.")
            self.firstArrival = False
        while True:
            if Settings.goNextRoom:
                break
            Settings.player.choice = input("> ").lower()

            if commonChoiceObject.check_player_input(self.inventory):
                pass