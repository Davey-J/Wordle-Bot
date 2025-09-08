import pandas as pd
import numpy as np
import string
from collections import Counter
from wordle_lib import *

wordle_words = pd.read_csv('Word Data/wordle_words_entropy.csv')
wordle_words = wordle_words.sort_values("entropy", ascending=False)

known_count = {}
possible_positions = [list(string.ascii_lowercase),list(string.ascii_lowercase),list(string.ascii_lowercase),list(string.ascii_lowercase),list(string.ascii_lowercase)]
known_positions = ['','','','','']

print("Welcome to Wordle Solver:")
print()

print("Ideal First Guesses:")
print(wordle_words["word"].head().to_string(index=False))
wordle_words, known_positions, possible_positions = run_guess(wordle_words, known_positions, possible_positions)
print()

print("Ideal Second Guesses:")
print(wordle_words["word"].head().to_string(index=False))
wordle_words, known_positions, possible_positions = run_guess(wordle_words, known_positions, possible_positions)
print()

print("Ideal Third Guesses:")
print(wordle_words["word"].head().to_string(index=False))
wordle_words, known_positions, possible_positions = run_guess(wordle_words, known_positions, possible_positions)
print()

print("Ideal Fourth Guesses:")
print(wordle_words["word"].head().to_string(index=False))
wordle_words, known_positions, possible_positions = run_guess(wordle_words, known_positions, possible_positions)
print()

print("Ideal Fifth Guesses:")
print(wordle_words["word"].head().to_string(index=False))
wordle_words, known_positions, possible_positions = run_guess(wordle_words, known_positions, possible_positions)
print()

print("Ideal Sixth Guesses:")
print(wordle_words["word"].head().to_string(index=False))
wordle_words, known_positions, possible_positions = run_guess(wordle_words, known_positions, possible_positions)
print()

