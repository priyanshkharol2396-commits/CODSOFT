import string
import random

def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    characters = ""

    if use_letters:
        characters += string.ascii_letters   
    if use_digits:
        characters += string.digits         
    if use_symbols:
        characters += string.punctuation     

    if not characters:
        print("Error: You must select at least one character type.")
        return ""

    # password generate karo
    password = "".join(random.choice(characters) for _ in range(length))
    return password

# ---------- main program ----------
print("Password Generator")

# 1. User se length lo
length = int(input("Enter password length: "))

# 2. Complexity options
use_letters_input = input("Include letters (y/n)? ").lower() == "y"
use_digits_input = input("Include digits (y/n)? ").lower() == "y"
use_symbols_input = input("Include symbols (y/n)? ").lower() == "y"

# 3. Password banao
pwd = generate_password(length, use_letters_input, use_digits_input, use_symbols_input)

# 4. Print password
if pwd:
    print("Generated password:", pwd)
