# HANGMAN GAME: MOVIE

* The classic hangman game where you will demonstrate that you know more movies titles than anyone else!
* The Hangman game randomly selects a movie title from the file 'words.txt' , and you have up to 7 incorrect letter guesses in each round before the stick man gets it!
* The user can add a movie to the file 'words.txt' if they wish to.
* The user is given the name of the movie director as a hint to help them guess the movie.

### Files included

| Index | Files | Description|
|-------|-------|------------|
| 1 | hangman_code.py | This is the main file which needs to be run for playing the game |
| 2 | hangman_draw.py | This file contains the various stages of hangman during the game and is imported in hangman_code.py |
| 3 | words.txt | This text file contains the names of the movies from which the program randomly choose a name for user to guess |
| 4 | test_hangman_code.py | This is the pytest file for the hangman_code.py file |

### Instructions to run program

* All the files must be stored in the same directory
* Run the file hangman_code.py
* Guess the letters in the given movie
* The user will be provided a total of 7 lives. The lives will be reduced by 1 for each wrong guess.
* For every wrong guess the hangman stage would be one step closer to losing and would be displayed.
* The letters that user has already guessed would be displayed as well. If the user enters the same letter again, there will be no change in the state.
* The blanks in the movie name will be updated with the corresponding letter if the user guessed the letter right.
* At the end, the user is prompted to add a movie to the text file 'words.txt'. If they wish to,they can choose 'y' and add movie name and director. If not, choose 'n'.

Hangman wishes you all the best and hope you enjoy the game!!

<p align="center">
  <img width="200" height="200" src="https://github.com/Rohinik7/263994_MiniProject/blob/main/logo.png?raw=true">
</p>




