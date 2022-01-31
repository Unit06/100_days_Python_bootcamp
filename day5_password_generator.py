# Password Generator day 5 project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input('How many symbols would you like?\n'))
nr_numbers = int(input('How many numbers would you like?\n'))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# PASS!
password = ''
for _ in range(nr_letters):
    password += letters[random.randint(0, len(letters) - 1)]

for _ in range(nr_symbols):
    password += symbols[random.randint(0, len(symbols) - 1)]

for _ in range(nr_numbers):
    password += numbers[random.randint(0, len(numbers) - 1)]

# Найден в просторах интернета.
# создаёт объект и замешивает данные внутри него
shake_password = ''.join(random.sample(password, len(password)))

print(f"Here is your password: {shake_password}")