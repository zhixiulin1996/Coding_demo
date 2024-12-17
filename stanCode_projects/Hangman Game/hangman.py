"""
File: hangman_ext.py
Name: Zhi-Xiu Lin
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
# For this extension, we can suppose that user only have 7 chances
N_TURNS = 7


def main():
    """
    The algorithm refer to "assignment explanation" file.
    For this extension, a hangman pattern will show only when user enters a wrong word.
    """
    answer = random_word()
    dashed = ''
    # Generate a '-''s string with length being the same with answer
    for i in range(len(answer)):
        dashed += '-'
    count = N_TURNS  # Initialize while loop index
    while True:
        # Situation1: User consume all of the chances
        if count == 0:
            print('You are completely hung :(')
            break
        # Situation2: User successfully find the answer before consuming all of the chances
        if dashed == answer:
            print('You win!!')
            break
        print('The word looks like: ' + dashed)
        print('You have ' + str(count) + ' wrong guesses left.')
        guess = remove_illegal()
        # The following code is to judge the guess corrected or not
        if answer.find(guess) == (-1):
            print('There is no ' + guess + '\'s in the word.')
            count -= 1  # chances for user -1
            print_man(count)  # only if the user enter a wrong word, the hangman pattern will show
        else:
            # if user successfully find one of char, then the chance count will not decrease
            new_dashed = ''
            print('You are correct!')
            for i in range(len(answer)):
                if answer[i] == guess:
                    new_dashed += guess
                else:
                    new_dashed += dashed[i]
            dashed = new_dashed
    print('The answer is: ' + answer)


def remove_illegal():
    """
    To ensure user enters the right format of guess, then turn the guess into upper case and return guess
    : return guess: str, the char entered by user which will be an upper cased alphabet
    """
    while True:
        guess = input('Your guess: ')
        if len(guess) == 1 and guess.isalpha() == True:
            guess = guess.upper()
            break
        else:
            print('Illegal format.')
    return guess


def print_man(count):
    """
    I use a nested if-else condition to print the different status of hangman
    :param count: int, will be in the range 0~7 (8 states)
    """
    print('---------')
    print('|    |')
    if count < 7:
        print('|    0')
        if count < 6:
            print('|   /', end='')
            if count < 5:
                print('|', end='')
                if count < 4:
                    print('\\')
                    if count < 3:
                        print('|    |')
                        if count < 2:
                            print('|   /', end='')
                            if count < 1:  # count==0
                                print(' \\')
                            else:  # count==1
                                print('')
                        else:  # count==2
                            print('|')
                    else:  # count==3
                        for i in range(2):
                            print('|')
                else:  # count==4
                    print('')
                    for i in range(2):
                        print('|')
            else:  # count==5
                print('')
                for i in range(2):
                    print('|')
        else:  # count==6
            for i in range(3):
                print('|')
    else:
        for i in range(4):
            print('|')
    for i in range(2):
        print('|')
    print('-----')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
