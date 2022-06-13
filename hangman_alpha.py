import random

CAPITALS = ["La Cruz", "La Paz"]

# A list of characters
secret_Word = list(random.choice(CAPITALS))

# Converts all the letters in secret_word to lowercase in a set 
# letters is set!
letters = {char.lower() for char in secret_Word if char.isalpha()}
print(letters)

# for char in secret_Word:
#     if char.isalpha():
#         letters = {char.lower()}

guessed_letters = set()

dashes = ["_" if char.isalpha() else char for char in secret_Word]
print(dashes)

print(' '.join(dashes))
guess = input("\n please, enter a letter: ")

while guess:
    print(f"User choice: {guess}")
    # Convert input to lower case
    guess = guess.lower()
    # If this letter was guessed before:
    if guess in guessed_letters:
        print("You already guessed this letter.")
    else:
        guessed_letters.add(guess)

        # Check if this choice is in our word
        if guess in letters:
            # If we have this letter then change dashes
           
            for index, val in enumerate(secret_Word):
                # Of the user input
                if val.lower() == guess:
                    dashes[index] = val
        # The letter is wrong
        else: 
            print("That letter didn't fit")

    print(' '.join(dashes))
    guess = input("\nguess a letter: ")