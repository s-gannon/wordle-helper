import os
import time
import numpy as np

legal_words = []
letter_frequencies = [[0]*26, [0]*26, [0]*26, [0]*26, [0]*26]

ALL_WORDS_FILE = open("words_alpha.txt", "r")
all_words = ALL_WORDS_FILE.read().split("\n")   #split the list via newline char; now we have an array

for i, word in enumerate(all_words):
    if len(word) == 5:
        legal_words.append(word)

for i, word in enumerate(legal_words):  #for each word in the list
    for j, letter in enumerate(word):   #for each letter in the word
        letter_frequencies[j][ord(letter) - 97] += 1

def possible_words(guess, colors, possible_list=legal_words):   #double letters currently breaks it (i.e. if you have 2 s's and one is green but another is black)
    pos_words = []
    
    if len(guess) != 5:
        print("Error: known should be a string of length 5")
        return None
    for i, word in enumerate(possible_list):
        is_possible = True
        for j, letter in enumerate(word):   #iterate through every letter in the word
            if colors[j] == 'g':
                if guess[j] != letter:      #if the letter was green and the current letter of the word is not that letter
                    is_possible = False
            if colors[j] == 'y':
                if guess[j] not in word:    #if the letter was yellow and it is not in this word
                    is_possible = False
                if guess[j] == letter:      #if the letter was yellow and the current letter of the word IS that letter
                    is_possible = False
            if colors[j] == 'b':
                if guess[j] in word:        #if the black letter that we guessed is in the word
                    is_possible = False
        if is_possible:
            pos_words.append(word)
    return pos_words
        # if len(possible_chars) > 0:
        #     for i, letter in enumerate(possible_chars):
        #         if letter not in word:
        #             is_possible = False
        # if len(impossible_chars) > 0:
        #     for i, letter in enumerate(impossible_chars):
        #         if letter in word:
        #             is_possible = False
        # for j, letter in enumerate(word):
        #     if known[j] == '-':
        #         continue
        #     elif known[j] != word[j]:
        #         is_possible = False
        # if is_possible:
        #     pos_words.append(word)

if __name__ == "__main__":
    current_list = []
    current_guess = ""
    current_colors = ""
    while True:
        current_guess = input("Enter in the current guess: ").lower()
        current_colors = input("Enter in the current colors ((g)reen/(y)ellow/(b)lack): ").lower()

        current_list = possible_words(current_guess, current_colors, current_list if len(current_list) != 0 else legal_words)
        print(f"\nThe current possible words it can be are: {current_list}\n")
