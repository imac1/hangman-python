import random
import re
already_tried_letters = set('')

# PART 1
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
difficulty = "1" # sample data, normally the user should choose the difficulty


# STEP 2
# based on the chosen difficulty level, set the values 
# for the player's lives
word_to_guess = "Cairo" # sample data, normally the word should be chosen from the countries-and-capitals.txt
lives = 5 # sample data, normally the lives should be chosen based on the difficulty
dashes = '_ '*len(word_to_guess)

print(dashes)
word_to_guess_set = set(word_to_guess)
print(word_to_guess_set)
display_word_list = list(word_to_guess)

print(display_word_list)
# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" display "_ _ _ _ _"



# STEP 4
# ask the user to type a letter
# here you should validate if the typed letter is the word 
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions
correct_letters = set('')
guess = input("please enter a letter\n")
if guess.lower() in word_to_guess:
    correct_letters.add(guess)
elif guess.lower() in word_to_guess.lower():
    correct_letters.add(guess)

else:
    already_tried_letters.add(guess)


print(correct_letters)
print(already_tried_letters)




# STEP 5
# validate if the typed letter is already in the tried letters
# HINT: search on the internet: `python if letter in list`
# If it is not, than append to the tried letters
# If it has already been typed, return to STEP 5. HINT: use a while loop here
# this list will contain all the tried letters


# STEP 6
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".

for i, v in enumerate(word_to_guess):
    print('letter in w ' + v)
    if guess == v:
        dashes = dashes.replace(dashes[i], guess)
        # dashes = dashes[i:] + guess + dashes[i+1:]
        print('dashes'+dashes)
#print(dashes[i:] + v + dashes[i+1:])
# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.



# STEP 7
# check if the variable already_tried_letters already contains all the letters necessary
# to build the value in the variable word_to_guess. If so display a winning message and exit
# the app.
# If you still have letters that are not guessed check if you have a non negative amount of lives
# left. If not print a loosing message and exit the app.
# If neither of the 2 conditions mentioned above go back to STEP 4
