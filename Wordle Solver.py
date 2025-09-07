import pandas as pd
import numpy as np
import string
from collections import Counter


wordle_words = pd.read_csv('Word Data/wordle_words.csv')
column_probabilities = pd.read_csv('Word Data/column_probabilities.csv')
wordle_words = wordle_words.sort_values("log_likelihood", ascending=False)

known_count = {}
possible_positions = [list(string.ascii_lowercase),list(string.ascii_lowercase),list(string.ascii_lowercase),list(string.ascii_lowercase),list(string.ascii_lowercase)]
known_positions = ['','','','','']
column_pos = [[0,'first'],[1,'second'],[2,'third'],[3,'fourth'],[4,'fifth']]

def make_guess():
    print("Input your chosen guess:")
    guess = input().lower()
    print("Input the results here (G for green, Y for yellow, N for grey):")
    results = input().upper()
    print()
    return guess, results

def contains_required_letters(word):
    word_count = Counter(word)
    return all(word_count[letter] >= count for letter, count in Counter(known_count).items())

def check_letters(guess, response):
    new_knowns = {}
    for x in range(5):
        if response[x] == 'Y':
            if guess[x] in new_knowns:
                new_knowns[guess[x]] += 1
            else:
                new_knowns[guess[x]] = 1
            if guess[x] in possible_positions[x]:
                possible_positions[x].remove(guess[x])
        if response[x] == 'G':
            if guess[x] in new_knowns:
                new_knowns[guess[x]] += 1
            else:
                new_knowns[guess[x]] = 1
            known_positions[x] = guess[x]
        global known_count
        known_count = new_knowns

    for x in range(5):
        if response[x] == 'N':
            if guess[x] in possible_positions[x]:
                possible_positions[x].remove(guess[x])
                if guess[x] not in known_count:
                    for y in range(5):
                        if guess[x] in possible_positions[y]:
                            possible_positions[y].remove(guess[x])


def filter_words(word_df):

    word_df = word_df[word_df["word"].apply(lambda w: contains_required_letters(w))]

    for x in column_pos:
        if known_positions[x[0]] != '':
            word_df = word_df[word_df[x[1]] == known_positions[x[0]]]
        pattern = f"[^{''.join(possible_positions[x[0]])}]"
        print(pattern)
        print(word_df)
        word_df = word_df[~word_df[x[1]].str.contains(pattern)]
        print(word_df)

    return word_df

print(wordle_words)
print("Welcome to Wordle Solver:")
print()

print("Ideal First Guesses:")
print(wordle_words["word"].head().to_string(index=False))
first_guess = make_guess()
check_letters(first_guess[0], first_guess[1])
wordle_words = filter_words(wordle_words)
print()

print("Ideal Second Guesses:")
print(wordle_words["word"].head().to_string(index=False))
second_guess = make_guess()
check_letters(second_guess[0], second_guess[1])
wordle_words = filter_words(wordle_words)
print()

print("Ideal Third Guesses:")
print(wordle_words["word"].head().to_string(index=False))
third_guess = make_guess()
check_letters(third_guess[0], third_guess[1])
wordle_words = filter_words(wordle_words)
print()

print("Ideal Fourth Guesses:")
print(wordle_words["word"].head().to_string(index=False))
fourth_guess = make_guess()
check_letters(fourth_guess[0], fourth_guess[1])
wordle_words = filter_words(wordle_words)
print()

print("Ideal Fifth Guesses:")
print(wordle_words["word"].head().to_string(index=False))
fifth_guess = make_guess()
check_letters(fifth_guess[0], fifth_guess[1])
wordle_words = filter_words(wordle_words)
print()

print("Ideal Sixth Guesses:")
print(wordle_words["word"].head().to_string(index=False))
sixth_guess = make_guess()
check_letters(sixth_guess[0], sixth_guess[1])
wordle_words = filter_words(wordle_words)
print()