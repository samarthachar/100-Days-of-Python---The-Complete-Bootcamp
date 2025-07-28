#TODO 1. Create a dictionary in this format:
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
inp = input("Enter your sentence: ").upper()
lst = [phonetic_dict[letter] for letter in inp if letter in phonetic_dict]
print(lst)
