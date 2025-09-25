# say  we want to uppercase the vowels in a string
source = "hello fellow humans"
# print(source.replace("aeiou", "AEIOU")) # not how this work
# although we might want it to work

# replace string method
print(source.replace("a", "A")) # old, new
print(source.replace("e", "E"))
print(source.replace("i", "I"))
print(source.replace("o", "O"))
print(source.replace("u", "U"))
print(source) # nothing has been saved

# but we want to save these changes over time
source = source.replace("a", "A")
source = source.replace("e", "E")
source = source.replace("i", "I")
source = source.replace("o", "O")
source = source.replace("u", "U")
print("after iteratively updating", source)

# let's loop over the vowels and see what that looks like
source = "hello fellow humans"

for v in "aeiou": # v for vowel
    # print(v, v.upper()) # now that we know we can use this
    source = source.replace(v, v.upper())
    # print(source) # see how it prints when inside the for loop

print(source) # see the final product outside of the for loop

# now get it into a function

"""
1. what is the name? upper_vowel
2. what is the input? a single string called original
3. what does it do? uppercases the vowels in the string
4. what does it return? the modified string
"""
def upper_vowel(original):
    # original = original.replace()
    for v in "aeiou":
        original = original.replace(v, v.upper())
    return original

print(upper_vowel("here's some content banana"))

### let's play with more string methods

more_text = "here's some different text yaaaaay"
print("rent" in more_text) # True
# but maybe we want False because we didn't want to
# search for substrings
# we can use `in` in a more restrictive way
print(more_text.split())
words = more_text.split()
print("rent" in words) # False, not checking substrings
print("some" in words) # True