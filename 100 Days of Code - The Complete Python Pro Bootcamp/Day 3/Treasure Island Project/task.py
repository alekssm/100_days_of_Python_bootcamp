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

choice = input("You are at a crossroad. Which way do you take - left or right?\n")

if choice == "left":
    choice = input("You come to a river bank. Do you swim or wait?\n")

    if choice == "wait":
        choice = input("You wait awhile and 3 magical doors appear before you, each with a different color. Which one do you choose to open - Red, Blue or Yellow?\n")
        if choice == "Yellow":
            print("You won!")
        elif choice == "Red":
            print("You are burned by fire - Game over!")
        elif choice == "Blue":
            print("You are eaten by beasts - Game over!")
        else:
            print("You didn't choose properly - Game over!")

    elif choice == "swim":
        print("You are attacked by a trout - Game over!")
    else:
        print("You didn't choose properly - Game over!")

elif choice == "right":
    print("You fell into a hole  - Game over!")
else:
    print("You didn't choose properly - Game over!")

