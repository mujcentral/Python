print('Welcome to love calculator')
name1=(input('What is your name? \n'))
name2=(input('What is the name of your love? \n'))
name1_len=len(name1)
name2_len=len(name2)
i=0
t=0
while (i < name1_len):
  if(name1[i]=='t' or name1[i]=='T'):
    t+=1
  if(name1[i]=='r' or name1[i]=='R'):
    t+=1
  if(name1[i]=='u' or name1[i]=='U'):
    t+=1
  if(name1[i]=='e' or name1[i]=='E'):
    t+=1
  i+=1
i=0
while (i < name2_len):
  if(name2[i]=='t' or name2[i]=='T'):
    t+=1
  if(name2[i]=='r' or name2[i]=='R'):
    t+=1
  if(name2[i]=='u' or name2[i]=='U'):
    t+=1
  if(name2[i]=='e' or name2[i]=='E'):
    t+=1
  i+=1
i=0
k=0
while (i < name1_len):
  if(name1[i]=='l' or name1[i]=='L'):
    k+=1
  if(name1[i]=='o' or name1[i]=='O'):
    k+=1
  if(name1[i]=='v' or name1[i]=='V'):
    k+=1
  if(name1[i]=='e' or name1[i]=='E'):
    k+=1
  i+=1
i=0
while (i < name2_len):
  if(name2[i]=='l' or name2[i]=='L'):
    k+=1
  if(name2[i]=='o' or name2[i]=='O'):
    k+=1
  if(name2[i]=='v' or name2[i]=='V'):
    k+=1
  if(name2[i]=='e' or name2[i]=='E'):
    k+=1
  i+=1
number=int(str(t)+str(k))
if (number<10 or number>90):
  print(f'Your score is {number}, you go together like coke and mentos.')
elif(number>40 and number<50):
  print(f'Your score is {number}, you are alright together.')
else:
  print(f'Your score is {number}.')
