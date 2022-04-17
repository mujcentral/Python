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
def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def div(n1,n2):
  return n1/n2
def multi(n1,n2):
  return n1*n2
operations={
  '+':add,
  '-':subtract,
  '/':div,
  '*':multi
  }
num1=float(input('Enter the first number: '))
num2=float(input('Enter the second number: '))
for keys in operations:
  print(keys)
good=1
while good==1:
  operation_symbol=input('Enter the operation symbol from the signs above: ')
  if (operation_symbol=='+' or operation_symbol=='-' or operation_symbol=='/' or operation_symbol=='*'):
    good=2
    first_ans=operations[operation_symbol](num1,num2)
  else:
    print('You entered a wrong symbol')
print(f'{num1} {operation_symbol} {num2} = {first_ans}')
choice='y'
while choice=='y':
  if input(f"Type 'y' to continue calculating with {first_ans} or type 'n' to exit :")=='y':
    num3=float(input('What is the next number: '))
    good=1
    while good==1:
      operation_symbol=input('Pick another operation: ')
      if (operation_symbol=='+' or operation_symbol=='-' or operation_symbol=='/' or operation_symbol=='*'):
        good=2
        second_ans=operations[operation_symbol](first_ans,num3)
      else:
        print('You entered a wrong symbol')
    print(f'{first_ans} {operation_symbol} {num3} = {second_ans}')
    first_ans=second_ans
  else:
    choice='n'