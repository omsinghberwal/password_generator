import random
import string

def generate_password(length=12, include_upper=True, include_numbers=True, include_special=True):
    characters = string.ascii_lowercase
    if include_upper:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    # Generate password by randomly selecting from the character set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator_app():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter password length (default is 12): ") or 12)
    except ValueError:
        print("Invalid input! Setting length to 12.")
        length = 12

    include_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    include_special = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, include_upper, include_numbers, include_special)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    password_generator_app()
