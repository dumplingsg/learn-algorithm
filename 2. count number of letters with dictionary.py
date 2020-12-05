# to create a dictionary to count the number of letters in a sentence

sentence = input()
new_dictionary = dict()

for letter in sentence:
    new_dictionary[letter] = new_dictionary.get(letter, 0)+1

print(new_dictionary)
