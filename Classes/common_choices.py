import Classes.settings as Settings
class CommonChoices():
    def __init__(self):
        pass

    def check_player_input(self):
        if self.check_inventory_input() or self.check_help_input()      \
            or self.check_bike_input() or self.check_read_note_input()  \
            or self.check_pick_key_input() or self.check_go_input():
                return True
        
    def check_inventory_input(self):
        if "inventory" in Settings.player.choice:
            Settings.player.inventory.print_all()
            # if "pizzaHub_key" in player.inventory:
            #     print(inventory["pizzaHub_key"])
            # else:
            #     if len(inventory) == 0:
            #         print("nothing there")
            return True

    def check_help_input(self):
        if "help" in Settings.player.choice:
            print("Help yourself Geez.")
            return True
    
    def check_bike_input(self):
        if "bike" in Settings.player.choice:
            if "get down" in Settings.player.choice or "leave" in Settings.player.choice or "get off" in Settings.player.choice:
                #TODO: chekBikeAvailability
                return True
            elif "climb" in Settings.player.choice or "ride" in Settings.player.choice or "get on" in Settings.player.choice:
                #TODO: chekBikeAvailability
                return True
        
    def check_read_note_input(self):
        if "read" in Settings.player.choice and "note" in Settings.player.choice:
            print("You got 4 hours and 100 pizzas to deliver! Make sure you serve them hot! Now, get busy (the note is sticky, for some reason)")

    def check_pick_key_input(self):
        if "pick" in Settings.player.choice and "key" in Settings.player.choice:
            if not Settings.player.inventory.check_item_exist("I001"):
                #TODO: add if key.position == player.position
                Settings.player.inventory.add_item("I001", "key", 1)
                print("Key added to your inventory")
                return True
            else:
                print("You already have the key.")
                return True
    
    def check_go_input(self):
        if "go" in Settings.player.choice:
            if "south" in Settings.player.choice:
                if(Settings.street_in_boundary(Settings.player.position[0] + 1, \
                                                Settings.player.position[1])):
                    Settings.player.position[0] = Settings.player.position[0] + 1
                    Settings.print_address()
                                                #TODO: add start_dialog
                else:
                    print("place out of bounds")

            elif "north" in Settings.player.choice:
                if(Settings.street_in_boundary(Settings.player.position[0] - 1, \
                                                Settings.player.position[1])):
                    Settings.player.position[0] = Settings.player.position[0] - 1
                    Settings.print_address()
                                                #TODO: add start_dialog
                else:
                    print("place out of bounds")

                
                #two_three_position()
            elif "west" in Settings.player.choice:
                if(Settings.street_in_boundary(Settings.player.position[0], \
                                                Settings.player.position[1] + 1)):
                    Settings.player.position[1] = Settings.player.position[1] + 1
                    Settings.print_address()
                                                #TODO: add start_dialog
                else:
                    print("place out of bounds")
                
                #three_four_position()
            elif "east" in Settings.player.choice:
                if(Settings.street_in_boundary(Settings.player.position[0], \
                                                Settings.player.position[1] - 1)):
                    Settings.player.position[1] = Settings.player.position[1] - 1
                    Settings.print_address()
                                                #TODO: add start_dialog
                else:
                    print("place out of bounds")
                
                #three_two_position() 
            
        else:
            print("Pardon me?")