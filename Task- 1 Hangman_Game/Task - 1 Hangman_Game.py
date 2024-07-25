# Importing Random module for choosing random word
import random

# List of words
word_list = ["light",
             "aftershock",
             "mango",
             "algorithm",
             "rice",
             "rose",
             "background",
             "consumable",
             "duplicate",
             "python"]

word = random.choice(word_list)  # selecting random word from the list

blank_list = []  # creating a blank list for displaying words with empty letters
for a in word:
    blank_list.append("_")
duplicate_list = blank_list.copy()
print(f"{' ':{'*'}^60}")
print(f"{'WELCOME TO THE HANGMAN GAME':{' '}^60}")
print(f"{' ':{'*'}^60}")
name = input("Enter player name:- ")  # Taking name of player
print()
print(f"{f'Welcome {name}':{' '}^60}")
print()
print(f"{' ':{'*'}^60}")  # Instructions of the game
print("!!!Read all the instructions carefully!!!"
      "\nInstructions of the game:-"
      "\n\n01. You will have to guess word from entering letters one by one."
      "\n02. Enter only one letter at a time."
      "\n03. Don't enter numbers, symbols or multiple letters at a time."
      "\n04. Each word is made up of unique letters and there is no repetition of same letter within the word."
      "\n05. Don't enter a letter again if it was already matched with word."
      "\n06. You have 6 chances to complete the game."
      "\n07. For every wrong answer your chances will be decreased by 1."
      "\n08. For every correct answer your chances will remain same."
      "\n09. If you guessed the word within chances then you will won the game."
      "\n10. If you exhaust your all chances then you will lose the game."
      "\n11. If your 1st guessed letter isn't found in the word then you have to restart the game.")
print(f"{' ':{'*'}^60}")

guesses = 6  # number of chances player have

# loop for running code again and again
while guesses > 0:
    guess_letter = input("\nEnter a letter : ")  # taking any one letter from the user
    guess_letter = guess_letter.lower()
    # Applying conditions according to rules of game
    if guess_letter in word:
        print(f"\nCongratulations {name}, you have guessed a letter of the word")
        print(f"\nChances left : {guesses}")
        for a in range(len(word)):
            if word[a] == guess_letter:
                blank_list[a] = guess_letter
                print(blank_list)
    elif guess_letter not in word and blank_list == duplicate_list:
        print("\nYour entered letter aren't found in word.\n"
              "Kindly start the guess again.")
        break

    elif guess_letter not in word:
        guesses -= 1
        print(f"\nWrong guess!!!\n Now you have only {guesses} chance left\n")
        print(blank_list)
    if blank_list == list(word):
        print(f"\nCongratulations {name}, You have won the game.\n")
        print(f"{' ':{'*'}^60}")
        break
if guesses == 0:
    print(f"{' ':{'*'}^60}")
    print("\n!!!Game Over!!!\nYou have lost the game.")
    print(f"{word} was the word.\n")
    print(f"{' ':{'*'}^60}")
# End of Code
