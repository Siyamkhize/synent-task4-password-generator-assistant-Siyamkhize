import random
import string

UPPERCASE_LETTERS = string.ascii_uppercase
LOWERCASE_LETTERS = string.ascii_lowercase
NUMBERS = string.digits
SPECIAL_CHARACTERS = string.punctuation

def generate_password(length):
    all_characters = UPPERCASE_LETTERS + LOWERCASE_LETTERS + NUMBERS + SPECIAL_CHARACTERS
    password = []

    if length >= 4:
        # Ensure at least one of each character type
        password.append(random.choice(UPPERCASE_LETTERS))
        password.append(random.choice(LOWERCASE_LETTERS))
        password.append(random.choice(NUMBERS))
        password.append(random.choice(SPECIAL_CHARACTERS))

        # Fill the rest of the password length
        for _ in range(length - 4):
            password.append(random.choice(all_characters))
    else:
        # Just pick from all characters for short passwords
        for _ in range(length):
            password.append(random.choice(all_characters))

    random.shuffle(password)
    return "".join(password)

def main():
    while True:
        try:
            length = int(input("Enter a number between 1 and 30: "))
            if length < 1 or length > 30:
                print("The number must be between 1 and 30.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()