# Password Generator (Radnom version)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
a = [random.choice(letters) for i in range(nr_letters)]
c = [random.choice(numbers) for i in range(nr_numbers)]
e = [random.choice(symbols) for i in range(nr_symbols)]
passwd_list = []
for i in a:
    passwd_list.append(i)
for j in c:
    passwd_list.append(j)
for k in e:
    passwd_list.append(k)
random.shuffle(passwd_list)
for l in passwd_list:
    print(l, end="")
print()
