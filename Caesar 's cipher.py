from random import *

strings = str(input())
new_strings = ''
x = randint(1, 26)

eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(strings)):
    if strings[i].isupper():
        n = eng_upper_alphabet.find(strings[i])
        while not n + x < len(eng_upper_alphabet):
            eng_upper_alphabet += eng_upper_alphabet
        new_strings += eng_upper_alphabet[n + x]
    elif strings[i].islower():
        n = eng_lower_alphabet.find(strings[i])
        while not n + x < len(eng_lower_alphabet):
            eng_lower_alphabet += eng_lower_alphabet
        new_strings += eng_lower_alphabet[n + x]
    else:
        new_strings += strings[i]

print(new_strings)
