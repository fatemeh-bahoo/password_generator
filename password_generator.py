import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v' , 'w','x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(' , ')', '*' , '+']

print("Welcome to the Python Password Generator!")
letter = int(input("How many letters would you like in your password?\n"))
symbol = int(input("How many symbols would you want?\n"))
number = int(input("How many numbers would you want?\n"))

# Simple way
# password = ""
# for character in range(0, letter):
#     password += random.choice(letters)

# for character in range(0, symbol):
#     password += random.choice(symbols)

# for character in range(0, number):
#     password += random.choice(numbers)

# print(f"Your password is: {password}")

# Hard way
password_list = []
for character in range(0, letter):
    password_list.append(random.choice(letters))

for character in range(0, symbol):
    password_list.append(random.choice(symbols))

for character in range(0, number):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = ""
for character in password_list:
    password += character

print(f"You password is: {password}")