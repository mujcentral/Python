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
alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(string,shift):
  list1=[]
  for i in range(len(string)):
    for m in range(len(alphabets)):
      if (string[i]==' '):
        list1.append(' ')
        break;
      elif(string[i]==alphabets[m]):
        try:
         list1.append(alphabets[m+shift])
        except:
          list1.append(alphabets[m+shift-26])
  return ''.join(list1)
def decrypt(string,shift):
  list2=[]
  for i in range(len(string)):
    for m in range(len(alphabets)):
      if (string[i]==' '):
        list2.append(' ')
        break;
      elif(string[i]==alphabets[m]):
        try:
         list2.append(alphabets[m-shift])
        except:
          list2.append(alphabets[m-shift+26])
  return ''.join(list2)
option='yes'
while option=='yes':
  choice=input('\nType encode if you want to encrypt or decode if you want to decrypt.\n').lower()
  if (choice=='encode'):
    string=input('Enter your message.\n')
    shift=int(input('Enter the shift'))
    print(f'The encoded message is {encrypt(string,shift)}')
  elif(choice=='decode'):
    string=input('Enter your message.\n').lower()
    shift=int(input('Enter the shift'))
    print(f'The decoded message is {decrypt(string,shift)}')
  else:
    print('Enter the correct choice.')
  option=input('If you would like to contiue then type yes, otherwise type no.\n').lower()