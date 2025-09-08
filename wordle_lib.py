import pandas as pd
import numpy as np
import string
from collections import Counter
import itertools
np.seterr(invalid='ignore', divide='ignore')

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

def check_letters(guess, response, known_positions, possible_positions):
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

    return known_positions, possible_positions

def filter_words(word_df, known_positions, possible_positions):

    word_df = word_df[word_df["word"].apply(lambda w: contains_required_letters(w))]

    for x in range(5):
        if known_positions[x] != '':
            word_df = word_df[word_df["word"].str[x] == known_positions[x]]
        pattern = f"[^{''.join(possible_positions[x])}]"
        word_df = word_df[~word_df["word"].str[x].str.contains(pattern)]

    return word_df

def check_result_frequency(word, result, words):
    possibles = words
    if result == 'GGGGG':
        return 1
    for letter in range(5):
        if result[letter] == "G":
            possibles = possibles[possibles.str[letter] == word[letter]]
        elif result[letter] == "Y":
            possibles = possibles[possibles.str.contains(word[letter])]
            possibles = possibles[possibles.str[letter] != word[letter]]
        elif result[letter] == "N":
            possibles = possibles[~possibles.str.contains(word[letter])]
    return len(possibles)

def recalculate_entropy(words):
    letters = ["G", "Y", "N"]
    possible_results = itertools.product(letters, repeat=5)
    possible_results = [''.join(seq) for seq in possible_results]

    for possible_result in possible_results:
        words[f"{possible_result} Count"] = words["word"].apply(lambda w: check_result_frequency(w, possible_result, words["word"]))

    total_count = words.shape[1]
    words["entropy"] = words.drop(columns=["word"]).apply(lambda x: x / total_count * -np.log2(x / total_count), axis=1).sum(axis=1)
    words = words.sort_values("entropy", ascending=False)

    return words

def run_guess(words, known_positions, possible_positions):
    guess = make_guess()
    known_positions, possible_positions = check_letters(guess[0], guess[1], known_positions, possible_positions)
    words = filter_words(words, known_positions, possible_positions)
    print(words.shape[0])
    words = recalculate_entropy(words)
    return words, known_positions, possible_positions