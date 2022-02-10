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
print('Welcome to Treasure Island')
print('Your mission is to find the treasure😎\n')
left_right=input('You walk down a road in a dense jungle. The road splits into two in front of you. Which way would you like to go? Left or Right :\n').lower()
if(left_right.count('left')==1):
  swim_wait=input('You now come across a river. Would you like to swim or wait for a boat?\n').lower()
  if(swim_wait.count('wait')==1 or swim_wait.count('boat')==1):
    which_door=input('The boat takes you to a castle which has Red, Blue and Yellow coloured doors. Which color door would you pick?\n').lower()
    if(which_door.count('yellow')==1):
      print('You Win. You found the treasue. Congratulations🤩')
    elif(which_door.count('red')==1):
      print('Hot lava got poured over you from above!!! Game Over')
    elif(which_door.count('blue')==1):
      print('A very large ice block hit your head!!! Game Over')
  else:
    print('You got eaten by a crocodile!!! Game Over')
else:
  print('You got ran over by a truck!!! Game Over')