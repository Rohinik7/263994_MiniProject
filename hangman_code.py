"""
Hangman game : Movie
Guess the name of movie based on the hint given
Movies provided from the file 'words.txt'
Allows user to add movies to 'words.txt'
7 lives provided
"""

import random
from hangman_draw import lives_left
import string


def get_txt():
    words = {}
    movie_names=open('words.txt','r')       # get the movie names from the file words.txt
    for line in movie_names:
        line=line.strip("\n")
        lst=list(map(str,line.split(":")))
        key,value=lst[0],lst[1]
        words[key]=value
    return words


def add_txt(movie,director):
    movie_names = open('words.txt', 'a')  # write movie name to the file words.txt
    line="\n{}:{}".format(movie,director)
    movie_names.write(line)


def get_valid_word():
    words=get_txt()     # calls function get_txt
    word = random.choice(list(words.keys()))  # randomly chooses something from the list
    return word.upper(),words[word]  # return word and the hint word(director)


def initialize():
    word , Hint= get_valid_word()         # get_valid_word function called
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    lives = 7
    return word,Hint,word_letters,alphabet,used_letters,lives


def format_input(word_letters,used_letters):
    # Insert space between words
    if ' ' in word_letters:
        used_letters.add(' ')
        word_letters.remove(' ')
    return used_letters,word_letters


def display(word_letters,used_letters,Hint,lives,word):
    # getting user input
    # letters used
    # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
    print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
    # what current word is (ie W - R D)
    used_letters,word_letters=format_input(word_letters,used_letters)                # format_input function called
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print(lives_left[lives])
    print('Current word: ', ' '.join(word_list))
    print("Hint: Movie Director: ", Hint)


def user_input(word_letters,lives):
    # Take in user input
    user_letter = input('Guess a letter: ').upper()
    return user_letter


def update(user_letter,used_letters,word_letters,alphabet,lives):
    # update the blanks if user guessed the letter
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
            print('')
        else:
            lives = lives - 1      # takes away a life if wrong
            print('\nYour letter,', user_letter, 'is not in the word.')
    elif user_letter in used_letters:
        print('\nYou have already used that letter. Guess another letter.')
    else:
        print('\nThat is not a valid letter.')
    return used_letters,lives


def end(lives,word):
    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_left[lives])
        print('You died sorry, better luck next time! . The Movie was', word)
    else:
        print('YAY! You guessed the Movie', word, '!!')


def user_contribution():
    inp=input("Would you like to add movie ? (y/n)")
    if inp.lower()=="y":
        movie=input("Movie name: ")
        director=input("Director: ")
        add_txt(movie,director)          # call function add_txt to write movie to file
    else:
        exit()


def hangman():    # to call functions
    word, Hint , word_letters, alphabet, used_letters, lives = initialize()
    while len(word_letters) > 0 and lives > 0:
        display(word_letters, used_letters, Hint, lives, word)      # display function called
        user_letter = user_input(word_letters, lives)           # user_input function called
        used_letters,lives = update(user_letter, used_letters, word_letters, alphabet, lives)   # update function called
    end(lives, word)                  # end function called
    user_contribution()        # user_contribution function called


if __name__ == '__main__':
    hangman()
