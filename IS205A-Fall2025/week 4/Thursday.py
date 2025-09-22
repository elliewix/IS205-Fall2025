"""
1. what's the name? find_letter
2. what are the params? take in 2:
    one string of a word to search: input_word
    one string of a letter to find: letter
3. What does it do?
    lowercases the input word, lowercase the letter
    searches for that letter in that word
4. Returns True or False (as a boolean)
"""

def find_letter(input_word, letter):
    lower_word = input_word.lower()
    lower_letter = letter.lower()
    result = lower_letter in lower_word
    # we are NOT returning "True" or "False" as strings
    # but the booleans
    return result

# 3 words to test on: catch, carry, bat
print(find_letter("catch", "c")) # True
print(find_letter("carry", "c")) # True
print(find_letter("bat", "c")) # False

word = "cat"
letter_check = "e"

found = find_letter(word, letter_check)
print(found)

### for loops and some fun shorthand

import string

print(string.ascii_letters)

# for loop syntax
# we want to loop over string.ascii_letters
# we want to name the individual items l (for letter)

for l in string.ascii_letters:
    # print(l)
    print(l, find_letter("iSchool", l))
