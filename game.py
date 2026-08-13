name = input("hey there!, please enter your name: ")

print (f"wellcome to the game, {name}!")

choice = input("what kind of game do you want to play? survival, creative, adventure, or spectator? ")

if choice == "survival":
    print("you have chosen survival mode, good luck!")
elif choice == "creative":
    print("you have chosen creative mode, have fun and show your creativity!")
elif choice == "adventure":
    print("you have chosen adventure mode, enjoy your wonderful adventurous journey!")
else:
    print("you have chosen spectator mode, enjoy watching the game!") 

player1 = "prince"
player2 = "knight"
player3 = "wizard"

if choice == "spectator":
    spectate = input("who you want to spectate? player1, player2, or player3 ")
    if spectate == "player1":
        print("you are now spectating the player1 prince")
    elif spectate == "player2":
        print("you are now spectating the player2 knight")
    elif spectate == "player3":
        print("you are now spectating the player3 wizard")
