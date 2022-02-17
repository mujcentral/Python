import random, time
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the KsPassword Generator!🤩🤩\n")
nr_letters= int(input("How many letters would you like in your password?🤨\n")) 
nr_symbols = int(input(f"How many symbols would you like?🤨\n"))
nr_numbers = int(input(f"How many numbers would you like?🤨\n"))
addition=nr_letters+nr_symbols+nr_numbers
password=['' for i in range(addition)]
for i in range(nr_letters):
  password[i]=letters[random.randint(0,25)]
for i in range(nr_symbols):
  password[i+nr_letters]=symbols[random.randint(0,8)]
for i in range(nr_numbers):
  password[i+nr_letters+nr_symbols]=numbers[random.randint(0,9)]
random.shuffle(password)
print('Creating password...')
time.sleep(3)
print('Your password is %s . Enjoy😊' %''.join(password[i] for i in range(addition)))