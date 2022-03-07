
print('''
:=*%@@@@@@@@@@@@@@@@@@@@@@@@@.                        .@@@@@@@@@@@@@@@@@@@@@@@@@%*=: 
  .=#@@@@@@@@@@@@@@@@@@@@@@#           i    i           #@@@@@@@@@@@@@@@@@@@@@@#=.     
     .=@@@@@@@@@@@@@@@@@@@@@%:         #%%%%#         :%@@@@@@@@@@@@@@@@@@@@@=.        
        =@@@@@@@@@@@@@@@@@@@@@@%#######@@@@@@#######%@@@@@@@@@@@@@@@@@@@@@@=           
         :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:                         
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@             
          .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.             
         -%%###%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%###%%-             
                         .:-=+*%@@@@@@@@@@@@@@@@@@@@%*+=-:.                            
                                 :=#@@@@@@@@@@@@#=:                                    
                                    .+@@@@@@@@+.                                       
                                      .#@@@@#.                                         
                                        =@@=                                           
                                        'l'
  ________               ____        __                              ______          __   
 /_  __/ /_  ___        / __ )____ _/ /_____ ___  ____ _____        / ____/___  ____/ /__ 
  / / / __ \/ _ \______/ __  / __ `/ __/ __ `__ \/ __ `/ __ \______/ /   / __ \/ __  / _ \\
 / / / / / /  __/_____/ /_/ / /_/ / /_/ / / / / / /_/ / / / /_____/ /___/ /_/ / /_/ /  __/
/_/ /_/ /_/\___/     /_____/\__,_/\__/_/ /_/ /_/\__,_/_/ /_/      \____/\____/\__,_/\___/                      ''')
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
