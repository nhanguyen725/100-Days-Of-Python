print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

crossroads = input("You're at a cross road. Where do you want to go?"
                   "Type 'left' or 'right' "). lower()
if crossroads == "left":
    lake = input("You've come to a lake. There is an island in the middle of the lake. "
                 "Type 'wait' to wait for a boat. Type 'swim' to swim across. "). lower()
    if lake == "wait":
        color = input("You arrived at the island unharmed. There is a house with 3 doors. "
                      "One red, one yellow, one blue. Which color do you choose? "). lower()
        if color == "yellow":
            food = input("You found a buffet. Which food do you choose? "
                         "Sushi, bibimbap, or bun cha? "). lower()
            if food == "bibimbap":
                print("You have a free flight to Korea!")
            elif food == "sushi":
                print("You have a flight to Japan!")
            elif food == "bun cha":
                print("You have a free flight to Vietnam!")
        elif color == "red":
            print("You were burned by fire. Game over.")
        elif color == "blue":
            print("You were eaten by beasts. Game over.")
        else:
            print("Game over.")
    else:
        print("You were attacked by a trout. Game over.")
else:
    print("Fall into a hole. Game over.")


