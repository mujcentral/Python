import random
import time
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
forward='yes'
uscore=0
cscore=0
game=[rock,paper,scissors]
print('Welcome to Rock, Paper, Scissors game😊\n')
while forward=='yes':
  number=random.randint(0,2)
  choice=input('What would you like to choose?\n').lower()
  while choice!='rock' and choice!='paper' and choice!='scissors':
      choice=input('Invalid entry. Enter again: ')
  if(choice=='rock'):
      if(game[number]==rock):
          print(f'Your choice👇\n{rock}')
          print('AI is selecting...')
          time.sleep(3)
          print(f"AI's choice👇\n{game[number]}")
          print(f"<<<Your score is: {uscore}>>>\n<<<AI's score is: {cscore}>>>")
      elif(game[number]==paper):
          print(f'Your choice👇\n{rock}')
          print('AI is selecting...')
          time.sleep(3)
          print(f"AI's choice👇\n{game[number]}")
          cscore+=1
          print(f"<<<Your score is: {uscore}>>>\n<<<AI's score is: {cscore}>>>")
      else:
          print(f'Your choice👇\n{rock}')
          print('AI is selecting...')
          time.sleep(3)
          print(f"AI's choice👇\n{game[number]}")
          uscore+=1
          print(f"<<<Your score is: {uscore}>>>\n<<<AI's score is: {cscore}>>>")  
  if(choice=='paper'):
      if(game[number]==rock):
          print(f'Your choice👇\n{paper}')
          print('AI is selecting...')
          time.sleep(3)
          print(f"AI's choice👇\n{game[number]}")
          uscore+=1
          print(f"<<<Your score is: {uscore}>>>\n<<<AI's score is: {cscore}>>>")
      elif(game[number]==paper):
          print(f'Your choice👇\n{paper}')
          print('AI is selecting...')
          time.sleep(3)
          print(f"AI's choice👇\n{game[number]}")
          print(f"<<<Your score is: {uscore}>>>\n<<<AI's score is: {cscore}>>>")
      else:
          print(f'Your choice👇\n{paper}')
          print('AI is selecting...')
          time.sleep(3)
          print(f"AI's choice👇\n{game[number]}")
          cscore+=1
          print(f"<<<Your score is: {uscore}>>>\n<<<AI's score is: {cscore}>>>")
  if(choice=='scissors' or choice=='scissor'):
      if(game[number]==rock):
          print(f'Your choice👇\n{scissors}')
          print('AI is selecting...')
          time.sleep(3)
          print(f"AI's choice👇\n{game[number]}")
          cscore+=1
          print(f"<<<Your score is: {uscore}>>>\n<<<AI's score is: {cscore}>>>")
      elif(game[number]==paper):
          print(f'Your choice👇\n{scissors}')
          print('AI is selecting...')
          time.sleep(3)
          print(f"AI's choice👇\n{game[number]}")
          uscore+=1
          print(f"<<<Your score is: {uscore}>>>\n<<<AI's score is: {cscore}>>>")
      else:
          print(f'Your choice👇\n{scissors}')
          print('AI is selecting...')
          time.sleep(3)
          print(f"AI's choice👇\n{game[number]}")
          print(f"<<<Your score is: {uscore}>>>\n<<<AI's score is: {cscore}>>>")  
  forward=input('Would you like to play more?(Yes or no)\n').lower()

if uscore>cscore:
  print('You Win👏👏👏')
elif uscore==cscore:
  print('It is a tie😅😅😅')
else:
    print('You lose. Better luck next time😊😊😊')


