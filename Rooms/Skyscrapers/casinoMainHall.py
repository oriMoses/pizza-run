from Classes.quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Skyscrapers_Street_Number, Skyscrapers_Street_Name, Colors
from Constants.constants import *
import random

class CasinoMainHall(skyscrapersQuarter):
    def __init__(self):
        skyscrapersQuarter.__init__(self, [Skyscrapers_Street_Name.LUCK,Skyscrapers_Street_Number.VI])
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)
        self.wins_with_shiny_dice = 0
        
    def __str__(self):
        return f"Casino Main Hall (floor 1)"

    def print_first_arrival(self):
        print("\nThe heart of the casino… at least the middle of it. \n\nYou see a dice table in the middle of the room. \nThe dice dealer is staring at you, for some reason. \n\nThere's an elevator to the", end=" ")
        print(Colors.UNDERLINE + "North" + Colors.END, end=" ")
        print(".")

        Settings.print_objects_in_room(self)
        

    def first_arrival(self, player):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("\nThe dice dealer is staring at you, for some reason.\n")
            Settings.print_objects_in_room(self)

    def win_dice_roll(self):
        print('You won 10 coins! \n"Nice roll! care for another round?"\n\nRoll again? yes\no')
        Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) + 10)

        if 'no' not in Settings.player.choice:
            Settings.player.choice = ''
            
        while Settings.player.choice != "yes" and Settings.player.choice != "no":
            Settings.player.choice = input("> ").lower()
        if 'yes' in Settings.player.choice:
            self.roll_dice()
        if 'no' in Settings.player.choice:
            print('"leaving with a win? a fine decision"')
        
    def loss_dice_roll(self):
        print('You lost!\n"Better luck next time… care for another round?" \n\nRoll again? yes\no')
        if 'no' in Settings.player.choice:
            print('"Don', end='')
            print("'", end='')
            print('t let it get you down kid, it just money"')
        if 'yes' in Settings.player.choice:
            self.roll_dice()
        
    def roll_dice(self):
        dice_number = random.uniform(0.0, 1.0)
        if dice_number < 0.5:
            self.win_dice_roll()
        else:
            self.loss_dice_roll()

    def roll_shiny_dice(self):
        print("You take the shiny dice out of your pocket… \n\nLets roll!!!")
        print('You won 10 coins! \n"Nice roll! care for another round?"\n\nRoll again? yes\no')
        Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) + 10)
        self.wins_with_shiny_dice +=1

    def player_caught_cheating(self):
        print('"You ca', end='')
        print("n't lose! Can", end='')
        print('you?" \n"Tell you what, ', end='')
        print("there's a high roller table in the V.I.P ", end='')
        print('section." \n\nA security guard shows up, he escorts you through several doors that are clearly not meant for V.I.P guests. \n\n"Nice little trick you got there. I', end='')
        print("haven't seen one of these in a long", end='')
        print('time." \n\nThe guard takes your shiny dice and leaves you at the casino parking lot.')

    def start_gambling(self):
        print('"What dice would you like to use?" \n"', end="")
        print("I've got a regular dice if you don't own any", end='')
        print('"\n\n**choose a dice!**')
        
        while Settings.player.choice != "regular dice" and Settings.player.choice != "shiny dice":
            Settings.player.choice = input("> ").lower()

            if "regular dice" in Settings.player.choice:
                print("The dealer gives you a regular dice.\n\nLet's roll!")

                self.roll_dice()


                #TODO: continuw from here
                
            elif "shiny dice" in Settings.player.choice:
                Settings.player.choice = ''

                self.roll_shiny_dice()
                
                while Settings.player.choice != "yes" and Settings.player.choice != "no":
                    Settings.player.choice = input("> ").lower()
                    if "yes" in Settings.player.choice:
                        if self.wins_with_shiny_dice == 4:
                            self.player_caught_cheating()

                        self.roll_shiny_dice()

                    elif "no" in Settings.player.choice:
                        if self.wins_with_shiny_dice > 0:
                            print("leaving with a win? a fine decision\n")
                    
                    Settings.player.choice = ''

            else:
                print("I've got a regular dice if you don't own any")
                print('"\n\n**choose a dice!**')
        
    def interaction_with_dealer(self):
        print('"Welcome, new face." \n"Its 5 coins per roll, 10 coins reward if you win" \n\n"Care for a play?" (will cost 5 coins) \n\nYes/No\n')
        while Settings.player.choice != "yes" and Settings.player.choice != "no":
            Settings.player.choice = input("> ").lower()

            if "yes" in Settings.player.choice:
                self.start_gambling()
                
            elif "no" in Settings.player.choice:
                print('"Alright, see you later. \nBy the way, you wanna check out the top floor" \n\nThe dealer wink at you, then greet the new gamblers and leave you to be.')
            else:
                print('"Care for a play?" (will cost 5 coins) \n\nYes/No\n')


        #TODO: continue from here!

    def dialog_circle(self, handleChoiceObject, player):
        self.first_arrival(player)
        print("DEBUG: TODO: not show location of main casino hall")
        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

            if ("go" in player.choice and "table" in player.choice) or ("talk" in player.choice and "dealer" in player.choice):
                self.interaction_with_dealer()
                
            elif handleChoiceObject.player_input(self.inventory, self.inputLegit):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False