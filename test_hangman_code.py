"""Pytest for hangman_code"""


import hangman_code as h
import random
import string


def test_format_input():
    word_letters = {'A', 'B', 'C', ' ', 'D'}
    used_letters = {'U', 'S', 'E', 'D'}
    used_letters, word_letters = h.format_input(word_letters, used_letters)
    assert word_letters == {'A', 'B', 'C', 'D'} and used_letters == {' ', 'D', 'E', 'S', 'U'}


def test_get_valid_word():
    words = h.get_txt()
    random.seed(53)
    word, hint = h.get_valid_word(words)
    assert word == "JOKER" and hint == "Todd Phillips"


def test_update1():
    user_letter = "E"
    alphabet = set(string.ascii_uppercase)
    word_letters = {'U', 'S', 'E', 'D'}
    used_letters = {'A', 'B', 'C', 'D'}
    lives = 1
    used_letters, lives = h.update(user_letter, used_letters, word_letters, alphabet, lives)
    assert used_letters == {'A', 'B', 'C', 'D', 'E'} and word_letters == {'U', 'S', 'D'}


def test_update2():
    user_letter = "W"
    alphabet = set(string.ascii_uppercase)
    word_letters = {'U', 'S', 'E', 'D'}
    used_letters = {'A', 'B', 'C', 'D'}
    lives = 1
    used_letters, lives = h.update(user_letter, used_letters, word_letters, alphabet, lives)
    assert lives == 0



