import random, time
row1=['🗳️','🗳️','🗳️']
row2=['🗳️','🗳️','🗳️']
row3=['🗳️','🗳️','🗳️']
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
location=int((input('At what place would you like to store your message?(column,row)\n')))
column=int(location/10)-1
row=int(location%10)-1
print('Accessing the location...')
time.sleep(3)
message=input('What message would you like to store? \n')
map[row][column]=message
print(f'Your message has been stored👇\n{row1}\n{row2}\n{row3}')