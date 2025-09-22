"""
1. What was the name? find_x
2. What were the params? word to search called input_word
3. What does it do? searches that word for the letter x,
    upper or lower case
4. What should it return? True or False, as a boolean
"""

def find_x(input_word):
    lower_word = input_word.lower()
    result = "x" in lower_word
    return result

print(find_x("hello")) # False

"""
1. What is the name? find_letter
2. What are the params? input_word and letter
3. What should it do? search the word for that letter,
    ignoring case
4. What should it return? True or False as a boolean
"""
def find_letter(input_word, letter):
    lower_word = input_word.lower()
    lower_letter = letter.lower()
    result = lower_letter in lower_word
    return result

print(find_letter("iSchool", "s")) # True
print(find_letter("GIES", "s")) # True
print(find_letter("LAS", "s")) # True

search_this = "School of Social Work"
for_this = "d"
print(find_letter(search_this, for_this))

# string module
import string

print(string.ascii_letters)
# print(string.whitespace)

# for loops
# 1. what are you looping over? string.ascii_letters
# 2. what will come out of it? individual characters, called l

for l in string.ascii_letters:
    print(l, find_letter(search_this, l))