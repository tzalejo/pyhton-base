# -*- coding: utf-8 -*-
import os
import random
IMAGEN= ['''
    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''

        ''']
WORDS = ['santiago']

def display_board(hidden_word, tries):
    print(IMAGEN[tries])
    print('')
    print(hidden_word)


def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]


def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        os.system('clear')
        display_board(hidden_word, tries)

        print('----*' * len(word))
        current_letter = str(input('Escoge una letra: '))

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)
        if len(letter_indexes) == 0:
            tries += 1
            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('Perdiste!!! La palabra era {}'.format(word))
                print('')
                break

        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []
        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('Felicidades Ganaste!!!')
            print('')
            break



if __name__ == '__main__':
    print('B I E N V E N I D O S   A   A H O R C A D O S ')
    run()

