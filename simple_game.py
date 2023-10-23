### ------------ VARIABLES ------------ ###

# Player Stat Variables
name = ""
level = 1
exp = 12
exp_level_up = 20
attack = 12

# Gameplay Variables
place = "town"
places = ["town", "inn", "shop"]
is_playing = 1

# Stats Menu Function
def stats_menu():
    print("Here is your stats")
    print("--------------- STATUS ---------------")
    print("Name     : " + str(name))
    print("Level    : " + str(level))
    print("Exp      : " + str(exp) + " / " + str(exp_level_up) + " (" + str(int(exp/exp_level_up*100)) + "%)")
    print("Attack   : " + str(attack))
    print("--------------------------------------")

### ------------ GAME STARTS HERE ------------ ###

print(" ~~~~~~~~~~~~~~~~~ DUNGEON EXPLORERS ~~~~~~~~~~~~~~~~~ ")
print("Hello, whats ur name?")
name = input()
print("Hi, nice to meet you " + name)
print("You shall start your journey...")

# While loop, do something according to place. will run as long as game running with is_playing
while is_playing:
    print("=============== " + place + " ===============")

    if place == "town":
        print("What do you want to do in town " + name)

    elif place == "shop":
        print("What do you want to buy?")

    elif place == "dungeon":
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
    
    # ask to move to another place
    print("Where do you want to go?")
    print("[1] go to shop, [2] go to dungeon, [9] check stats, [0] stop playing")
    goto = int(input())

    # if-else to change place
    if goto == 1:
        place = "shop"
        print("moving to shop")
    elif goto == 2:
        place = "dungeon"
        print("moving to dungeon")
    elif goto == 9:
        stats_menu()
    elif goto == 0:
        print("game exit")
        is_playing = 0
    else:
        print ("you input the wrong number")

### ------------ GAME ENDS HERE ------------ ###