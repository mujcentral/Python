print('Welcome to Python Pizza Delivery')
size = input('What size do you want to order pizza? ')
add_pepperoni=input('Do you want pepperoni? ')
extra_cheese=input('Do you want extra cheese? ')
if (size[0].lower()=='l'):
  money=25
  if (add_pepperoni[0].lower()=='y'):
    money+=3
  if (extra_cheese[0].lower()=='y'):
    money+=1
elif (size[0].lower()=='m'):
  money=20
  if (add_pepperoni[0].lower()=='y'):
    money+=3
  if (extra_cheese[0].lower()=='y'):
    money+=1
else:
  money = 15
  if (add_pepperoni[0].lower()=='y'):
    money+=2
  if (extra_cheese[0].lower()=='y'):
    money+=1
print(f'You have to pay ${money}')
print('You have to pay $%d' % money)