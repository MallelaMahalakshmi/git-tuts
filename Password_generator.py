print("Welcome to the Password Generator (No Imports)")

# Step 1: Define character sets manually
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special = "!@#$%^&*()-_=+[]{};:,.<>/?"

# Step 2: Get password length
while True:
    try:
        length = int(input("Enter password length (min 4): "))
        if length < 4:
            print("Length must be at least 4!")
            continue
    except ValueError:
        print("Enter a valid integer!")
        continue
    break

# Step 3: Ask user for character type choices
include_lower = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
include_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
include_special = input("Include special characters? (yes/no): ").lower() == 'yes'

# Step 4: Validate at least one type selected
if not (include_lower or include_upper or include_digits or include_special):
    print("You must select at least one character type!")
else:
    # Combine chosen characters into one string
    characters = ""
    if include_lower:
        characters += lowercase
    if include_upper:
        characters += uppercase
    if include_digits:
        characters += digits
    if include_special:
        characters += special

    # Step 5: Create a custom random-like selection using simple math
    password = ""
    seed = len(characters) * length  # simple seed
    for i in range(length):
        seed = (seed * 1103515245 + 12345) % (2**31)  # pseudo-random formula
        index = seed % len(characters)
        password += characters[index]

    print("Your generated password is:", password)
