class Player():
    # static information
    name = ""

    # game stats
    level = 1
    exp = 20
    exp_level_up = 20
    attack = 12
    
    # game dynamic information
    place = "town"

    def stats_menu(self):
        print("Here is your stats")
        print("--------------- STATUS ---------------")
        print("Name     : " + str(self.name))
        print("Level    : " + str(self.level))
        print("Exp      : " + str(self.exp) + " / " + str(self.exp_level_up) + " (" + str(int(self.exp/self.exp_level_up*100)) + "%)")
        print("Attack   : " + str(self.attack))
        print("--------------------------------------")