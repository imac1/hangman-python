import random
import os
import HANGMAN_ASCII
from game_style import style
from game_style import animator
from game_style import exit
os.system("")

class style:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"


happy = ["h1.txt", "h2.txt", "h3.txt", "h4.txt"]
country_list = []
capital_list = []
easy_list = []
medium_list = []
hard_list = []
line_list = []

countries_and_capitals = open("countries-and-capitals.txt", "r")
for line in countries_and_capitals:
    chars = '.,!|'
    stripped_line = line.strip()
    line_list = stripped_line.split("|")
    country_list.append(line_list[0])
    capital_list.append(line_list[1])
    new_C_list = [elem for elem in capital_list if elem.strip()]
    new_CO_list = [elem for elem in country_list if elem.strip()]

for lenght in new_CO_list:
    if len(lenght) <= 5:
        easy_list.append(lenght)
    elif 5 < len(lenght) < 10:
        medium_list.append(lenght)
    elif len(lenght) >= 10:
        hard_list.append(lenght)

for lenght in new_C_list:
    if len(lenght) <= 5:
        easy_list.append(lenght)
    elif 5 < len(lenght) < 10:
        medium_list.append(lenght)
    elif len(lenght) >= 10:
        hard_list.append(lenght)


def getRandomWord(word_List):
    # This function returns a random string from the passed list of words
    word_Index = random.randint(0, len(word_List) - 1)
    return word_List[word_Index]


def displayBoard(HANGMAN_ASCII, missed_Letters, correct_Letters, secret_Word):
    print(HANGMAN_ASCII[len(missed_Letters)])
    print()
    print("Missed letters:", end=" ")
    for letter in missed_Letters:
        print(letter, end=" ")
    print()
    dashes = "_" * len(secret_Word)
    for i in range(len(secret_Word)):  # replace blanks with correctly guessed letters
        if secret_Word[i] in correct_Letters:
            dashes = dashes[:i] + secret_Word[i] + dashes[i + 1:]
    for letter in dashes:  # show the secret word with spaces in between each letter
        print(letter, end=" ")
    print()


def getGuess(letters_Guessed):
    # Returns the letter the player entered.
    # This function makes sure the player entered a single letter,
    # and not something else.
    while True:
        print("Guess a letter.")
        print(secret_Word)
        
        guess = input().lower()
        if len(guess) != 1:
            print(style.CYAN, "Please, enter a single letter")
        elif guess in letters_Guessed:
            print(style.RED, "You have already guessed that letter. Choose again.")
        elif guess not in "abcdefghijklmnopqrstuvxzwy":
            print("Please enter a LETTER.")
        else:
            return guess


def playAgain():
    # This function returns True if the player wants to play again,
    #  otherwise it returns False.
    print(style.RED, "Do you want to play again? (yes or no)")
    return input().lower().startswith("y")


print(style.GREEN, "H A N G M A N")
difficulty = "X"

while difficulty not in "EMH":
    
    print("Enter difficulty: E - Easy, M - Medium, H - Hard")
    print('................................................')
    print('E - 5 letters words    |     M - 7 letters words')
    print('............... H - 8 letters words ............')
    print("")
    difficulty = input().upper()
if difficulty == "E":
    words = easy_list
if difficulty == "M":
    del HANGMAN_ASCII.HANGMAN_PICS[8]
    del HANGMAN_ASCII.HANGMAN_PICS[7]
    words = medium_list
if difficulty == "H":
    del HANGMAN_ASCII.HANGMAN_PICS[8]
    del HANGMAN_ASCII.HANGMAN_PICS[7]
    del HANGMAN_ASCII.HANGMAN_PICS[5]
    del HANGMAN_ASCII.HANGMAN_PICS[3]
    words = hard_list
missed_Letters = ""
correct_Letters = ""
secret_Word = getRandomWord(words).lower().strip(' ')
print(secret_Word)

game_Finished = False

while True:
    displayBoard(HANGMAN_ASCII.HANGMAN_PICS, missed_Letters, correct_Letters, secret_Word)
    # Let the player type in a letter.
    guess = getGuess(missed_Letters + correct_Letters)
    # todo secret word must be lower (another variable thank secretWord)
    if guess in secret_Word:
        correct_Letters = correct_Letters + guess
        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secret_Word)):
            if secret_Word[i] not in correct_Letters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secret_Word.title() + '"! You have won!')
            animator(happy, delay=1, repeat=3)
            game_Finished = True
        else:
            missed_Letters = missed_Letters + guess
        # Check if player has guessed too many times and lost
        if len(missed_Letters) == len(HANGMAN_ASCII.HANGMAN_PICS) - 1:
            displayBoard(HANGMAN_ASCII.HANGMAN_PICS, missed_Letters, correct_Letters, secret_Word)
            print(
                "You have run out of guesses!\nAfter "
                + str(len(missed_Letters))
                + " missed guesses and "
                + str(len(correct_Letters))
                + ' correct guesses, the word was "'
                + secret_Word
                + '"'
            )
            game_Finished = True

    # Ask the player if they want to play again (but only if the game is done).
    if game_Finished:
        if playAgain():
            missed_Letters = ""
            correct_Letters = ""
            game_Finished = False
            secret_Word = getRandomWord(words).lower().strip(' ')
        else:
            break