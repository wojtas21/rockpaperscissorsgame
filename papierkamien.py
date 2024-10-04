import random


def play_game():
    rps = random.randint(1,3)

    print("==========Welcome to game!==========")
    print("")
    print("=========Rock Paper Scisors==========")
    print("")
    print("")

    print("+++++")

    print("1. Rock")
    print("2. Paper")
    print("3. Scisors")

    print("+++++")
    print("")
    print("")

    player_select = int(input("Make your choice (1-3): "))


    if rps == player_select:
        print("REMIS")
    elif (rps == 1 and player_select == 3) or\
         (rps == 2 and player_select == 1) or\
         (rps == 3 and player_select == 2):
         print("You've lost!")
    else:
        print("You've won!")
        
play_game()