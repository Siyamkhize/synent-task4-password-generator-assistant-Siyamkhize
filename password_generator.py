import random
import string

UPPERCASE_LETTERS = string.ascii_uppercase
LOWERCASE_LETTERS = string.ascii_lowercase
NUMBERS = string.digits
SPECIAL_CHARACTERS = string.punctuation

def generate_password(length, mode="Strong"):
    all_characters = UPPERCASE_LETTERS + LOWERCASE_LETTERS + NUMBERS + SPECIAL_CHARACTERS
    password = []

    if mode == "Super Strong":
        # Ensure at least 2 of each character type for Super Strong
        for _ in range(2):
            password.append(random.choice(UPPERCASE_LETTERS))
            password.append(random.choice(LOWERCASE_LETTERS))
            password.append(random.choice(NUMBERS))
            password.append(random.choice(SPECIAL_CHARACTERS))
        
        # Fill the rest
        for _ in range(length - 8):
            password.append(random.choice(all_characters))
    elif length >= 4:
        # Strong (Standard) mode
        password.append(random.choice(UPPERCASE_LETTERS))
        password.append(random.choice(LOWERCASE_LETTERS))
        password.append(random.choice(NUMBERS))
        password.append(random.choice(SPECIAL_CHARACTERS))

        for _ in range(length - 4):
            password.append(random.choice(all_characters))
    else:
        # Just pick from all characters for very short passwords
        for _ in range(length):
            password.append(random.choice(all_characters))

    random.shuffle(password)
    return "".join(password)

def main():
    while True:
        try:
            print("\nSelect Password Mode:")
            print("1. Strong (Balanced)")
            print("2. Super Strong (Extra character diversity)")
            mode_choice = input("Choice (1 or 2, default 1): ").strip()
            
            mode = "Super Strong" if mode_choice == "2" else "Strong"
            
            length = int(input("Enter a number between 1 and 30: "))
            if length < 1 or length > 30:
                print("The number must be between 1 and 30.")
                continue
            
            if mode == "Super Strong" and length < 8:
                print("Super Strong mode requires at least 8 characters. Falling back to Strong mode.")
                mode = "Strong"
                
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    password = generate_password(length, mode)
    print(f"\nMode: {mode}")
    print("Generated Password:", password)

if __name__ == "__main__":
    main()