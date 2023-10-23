from player import Player

class Game():
    # private variables
    player = Player()
    places = ["town", "inn", "shop"]
    is_playing = 1
    
    def __init__(self):
        self.game_intro()
        self.game_loop()

    def game_intro(self):
        print(" ~~~~~~~~~~~~~~~~~ DUNGEON EXPLORERS ~~~~~~~~~~~~~~~~~ ")
        print("Hello, whats ur name?")
        self.player.name = input()
        print("Hi, nice to meet you " + self.player.name)
        print("You shall start your journey...")

    def go_somewhere(self):
        print("Where do you want to go?")
        print("[1] go to shop, [2] go to dungeon, [8] check stats, [9] stop playing")
        goto = int(input())

        if goto == 1:
            self.player.place = "shop"
            print("moving to shop")
        elif goto == 2:
            self.player.place = "dungeon"
            print("moving to dungeon")
        elif goto == 9:
            self.player.stats_menu()
        elif goto == 0:
            print("game exit")
            self.is_playing = 0
        else:
            print ("you input the wrong number")

    def game_loop(self):
        while self.is_playing:
            print("=============== " + self.player.place + " ===============")

            if self.player.place == "town":
                print("What do you want to do in town " + self.player.name)

            elif self.player.place == "shop":
                print("What do you want to buy?")

            elif self.player.place == "dungeon":
                print("You are in the dungeons, be prepared!")
            
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("...Unfortunately, there is still nothing to do here, the developer has not implemented it yet...") # Currently what to do in each place has not been implemented, just give this 'sorry' message
            print("==============================")
            
            self.go_somewhere()

game = Game()