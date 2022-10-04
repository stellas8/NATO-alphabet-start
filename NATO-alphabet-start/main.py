# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# print(alphabet_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()

output_list = [alphabet_dict[letter] for letter in word]

print(output_list)