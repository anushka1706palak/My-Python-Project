import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    if not (use_upper or use_lower or use_digits or use_symbols):
        return "Error: At least one character type must be selected."

    character_pool = ''
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Python Password Generator!")
    try:
        length = int(input("Enter desired password length (e.g., 12): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()