import random
from hangman_guessing import guess_list
import string


def hangman():
    word = random.choice(guess_list)        #randomly chooses something from the list
    word = word.upper()                     #casting the word to upper case
    word_letters = set(word)                #letters in the word
    alphabet = set(string.ascii_uppercase)  #will be used for comparing if the entered letter is valid
    used_letters = set()                    #User has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letter used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print(display_hangman(lives))
        print(f'You have {lives} lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  #takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print(f'You have already used the {user_letter} charater. Please try again.')

        else:
            print("Invalid charater. Please try again.")

    # gets here when len(word_letters) == 0
    if lives == 0:
        print(display_hangman(lives))
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


def display_hangman(lives):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[lives]


if __name__ == '__main__':
    hangman()