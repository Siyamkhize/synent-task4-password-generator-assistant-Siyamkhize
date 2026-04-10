import random
import string

UPPERCASE_LETTERS = string.ascii_uppercase
LOWERCASE_LETTERS = string.ascii_lowercase
NUMBERS = string.digits
SPECIAL_CHARACTERS = string.punctuation

def generate_password(length, mode="Strong", include_upper=True, include_lower=True, include_numbers=True, include_special=True):
    pool = ""
    if include_upper: pool += UPPERCASE_LETTERS
    if include_lower: pool += LOWERCASE_LETTERS
    if include_numbers: pool += NUMBERS
    if include_special: pool += SPECIAL_CHARACTERS
    
    if not pool:
        return "Error: No characters selected!"

    password = []

    # Requirements list
    reqs = []
    if include_upper: reqs.append(UPPERCASE_LETTERS)
    if include_lower: reqs.append(LOWERCASE_LETTERS)
    if include_numbers: reqs.append(NUMBERS)
    if include_special: reqs.append(SPECIAL_CHARACTERS)

    if mode == "Super Strong":
        # Ensure at least 2 of each selected character type
        for char_set in reqs:
            password.append(random.choice(char_set))
            password.append(random.choice(char_set))
        
        # Fill the rest
        for _ in range(length - len(password)):
            password.append(random.choice(pool))
    elif length >= len(reqs):
        # Strong (Standard) mode - ensure at least one of each selected
        for char_set in reqs:
            password.append(random.choice(char_set))

        for _ in range(length - len(reqs)):
            password.append(random.choice(pool))
    else:
        # Just pick from selected pool for very short passwords
        for _ in range(length):
            password.append(random.choice(pool))

    random.shuffle(password)
    return "".join(password)

def main():
    while True:
        try:
            print("\n--- Password Generator Settings ---")
            
            # Character Set Options
            print("\nInclude Character Sets? (y/n):")
            u = input("Uppercase (A-Z)? [y]: ").lower() != 'n'
            l = input("Lowercase (a-z)? [y]: ").lower() != 'n'
            n = input("Digits (0-9)? [y]: ").lower() != 'n'
            s = input("Special characters (!@#$%^&*...)? [y]: ").lower() != 'n'
            
            if not (u or l or n or s):
                print("Error: You must select at least one character set!")
                continue

            # Mode Options
            print("\nSelect Password Mode:")
            print("1. Strong (Balanced)")
            print("2. Super Strong (Extra character diversity)")
            mode_choice = input("Choice (1 or 2, default 1): ").strip()
            mode = "Super Strong" if mode_choice == "2" else "Strong"
            
            length = int(input("\nEnter a number between 1 and 30: "))
            if length < 1 or length > 30:
                print("The number must be between 1 and 30.")
                continue
            
            # Super Strong validation
            min_req = (u+l+n+s) * 2 if mode == "Super Strong" else 1
            if mode == "Super Strong" and length < min_req:
                print(f"Super Strong mode with selected sets requires at least {min_req} characters. Falling back to Strong mode.")
                mode = "Strong"
                
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    password = generate_password(length, mode, u, l, n, s)
    print(f"\n--- Result ---")
    print(f"Mode: {mode}")
    print(f"Includes: {'U' if u else ''}{'L' if l else ''}{'N' if n else ''}{'S' if s else ''}")
    print("Generated Password:", password)

if __name__ == "__main__":
    main()