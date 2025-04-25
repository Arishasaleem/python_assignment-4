import random
import string

print("Welcome to the Password Generator!")

# Step 1: Get user preferences
length = int(input("Enter the desired password length: "))

include_letters = input("Include letters? (y/n): ").lower() == 'y'
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Step 2: Build character pool
characters = ''
if include_letters:
    characters += string.ascii_letters  
if include_numbers:
    characters += string.digits       
if include_symbols:
    characters += string.punctuation    

if not characters:
    print(" You must include at least one type of character.")
    exit()

password = ''.join(random.choice(characters) for _ in range(length))

print(f"\nYour generated password is:  {password}")
