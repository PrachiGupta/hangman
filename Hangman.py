#hangman game

import random

with open('words.txt') as f:
    words = f.read().split()
word = random.choice(words)

correct_guesses = set()
wrong_guesses = set()
max_guesses = 6

def guess_remaining():
    return max_guesses - len(wrong_guesses)

def has_lost():
    return guess_remaining() == 0

def has_won():
    return all(letter in correct_guesses for letter in word)

while not has_lost() and not has_won() :

    print("".join(letter if letter in correct_guesses else '-' for letter in word))
    print("{} guesses remaining".format(guess_remaining()))
    guess = input("Enter a letter :")
    if guess in word:
        correct_guesses.add(guess)
    else:
        wrong_guesses.add(guess)
    
if has_won():
    print("You guessed it right. The word is " + word)
else:
    print("The word is " + word + ".Better luck next time!")


