print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("-----------------------------------------")


#add the input for left/right
left_right = input("You came to a crossroads. would you like to turn \"Left\" or \"Right\"? \n").lower()
#if the user types left
if left_right == 'left':
  #add the input for swim/wait
  swim_wait = input('You\'ve gotten to a lake. Do you "Swim" or "Wait"? \n').lower()
  #if the user types wait
  if swim_wait == 'wait':
    #add input for which door to choose
    door = input('You have come across 3 doors, which do you choose?: "Red", "Blue", or "Yellow?" \n').lower()
    #elif for red door
    if door == 'red':
        print("You got burned by fire. Game Over")
    #elif for blue door
    elif door == 'blue':
      print("You were eaten by beasts. Game Over")
    #elif for yellow door
    elif door == 'yellow':
      print("Congratulations!!!!!! You win!!!!!")
    #else for if user types in something else
    else:
      print("Sorry, you fell into the lake and were eaten by a monster. Game Over.")
  #else for if user types in swim or something else
  else:
    print("Sorry, you got attacked by trout. Game Over")
#else for if user types in right or something else
else:
    print("Sorry, you fell into a hole. Game Over.")
