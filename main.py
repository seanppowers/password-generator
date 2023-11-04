#Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_chosen = ""
symbols_chosen = ""
numbers_chosen = ""

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
for i in range(nr_letters):
  letters_chosen += random.choice(letters)

nr_symbols = int(input(f"How many symbols would you like?\n"))
for i in range(nr_symbols):
  symbols_chosen += random.choice(symbols)

nr_numbers = int(input(f"How many numbers would you like?\n"))
for i in range(nr_numbers):
  numbers_chosen += random.choice(numbers)

generated_password = str(letters_chosen) + str(symbols_chosen) + str(numbers_chosen)
string_list = list(generated_password)
random.shuffle(string_list)
shuffled_string = ''.join(string_list)
print("Your new password is: " + shuffled_string)