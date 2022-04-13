import random
from words import words
import string

# print(words)


def get_valid_word(words):
    word = random.choice(words)  # randomly choose something from the listen
    # word should not contain '-' or space.
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what user has guessed

    lives = 6  # total lifes user has to predict the word

    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a','b','cd']) --> 'a b cd'
        print(" you have", lives, "lives left and you have used these letters: ",
              ' '.join(used_letters))

        # what the current word is (ie W - R D)
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # getting user input
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1  # takes away a life if wrong
                print("Letters is NOT in the word!")

        elif user_letter in used_letters:
            print("you have already used that character. Please try again..")

        else:
            print("Invalid characters. Please try again")

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print("you died sorry. the word was ", word)
    else:
        print("you gussed the word", word, "!!")


hangman()
