import random
names=input('Gimme da names: ')
names_input=names.split(', ')
random_names=len(names_input)
print(names_input[random.randint(0,random_names-1)], 'will pay the bill.')