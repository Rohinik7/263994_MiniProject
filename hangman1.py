"""
Hangman game : Movie
Guess the name of movie based on the hint given
7 lives provided
"""

import random
from word1 import words
from hangman_draw import lives_left
import string


def get_valid_word(words):
    word = random.choice(list(words.keys()))  # randomly chooses something from the list
    return word.upper()


def hangman():
    word = get_valid_word(words)
    Hint = words[word.capitalize()]  # the hint keyword(director)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        # what current word is (ie W - R D)
        if ' ' in word_letters:
            used_letters.add(' ')
            word_letters.remove(' ')
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_left[lives])
        print('Current word: ', ' '.join(word_list))
        print("Hint: Movie Director: ", Hint)

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_left[lives])
        print('You died sorry, better luck next time! . The Movie was', word)
    else:
        print('YAY! You guessed the Movie', word, '!!')


if __name__ == '__main__':
    hangman()
