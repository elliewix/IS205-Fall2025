source = "hello fellow humans"

# we want to upper case just the vowels
# vowels are aeiou
# we can use the .replace() method
# string.replace(oldstuff, newstuff)

# this won't work, but is a pretty natural
# desire to work
print(source.replace("aeiou", "AEIOU"))
# remember: replace works on one thing at a time
# we will need to use it once per vowel
print(source.replace('a', 'A'))
print(source.replace('e', 'E'))
print(source.replace('i', 'I'))
print(source.replace('o', 'O'))
print(source.replace('u', 'U'))

print(source) # see there are no changes

# we need to save the results to a variable
# and that should be the same variable to save
# all the changes together
source = "hello fellow humans"
source = source.replace('a', 'A')
# print(source) # now we will see the changes persist
source = source.replace('e', 'E')
source = source.replace('i', "I")
source = source.replace('o', 'O')
source = source.replace('u', 'U')
print('final result:', source)

# a) we can use a loop to repeatedly do stuff
# b) we can loop over the vowels because that's
#    what I'm messing with repeatedly from above

source = "hello fellow humans" # reset back to original

for v in "aeiou": # v for vowel for the variable name
    # print(v) # always check your work before you move on
    # print(v, v.upper()) # can we get the data we need? yes!
    source = source.replace(v, v.upper())
    # print(source) # see what happens when you print inside the loop
print("final result from loop", source) # see the final result here, after the for loop runs

######
different_text = "here's some different text yaaaay"
for v in "aeiou":
    # different_text = different_text.replace(v, v.upper() + v + v.upper())
    # not limited to changing just character, you can add
    different_text = different_text.replace(v, "")
print(different_text)

# for HW2 we'll need to do this for punctuation characters
import string
print(string.punctuation)

### let's get this into a string
"""
1. what should this be called? upper_vowels
2. what should the input be? a single string called original
3. what should it do? uppercase all the vowels
4. what should it return? a new string with those changes
"""
def upper_vowels(original):
    # act on original as if it holds the input content
    # because it will
    for v in "aeiou":
        original = original.replace(v, v.upper())
    return original # return instead of print, bc inside of a func
    # note the location and indent of this return

# we'll test this on the test cases from HW2

t1 = "***START OF THE PROJECT GUTENBERG EBOOK THREE YEARS IN EUROPE***"
t2 = "E-text prepared by Suzanne Shell, Michael Punch, and the Project Gutenberg"
t3 = "MEMOIR OF WILLIAM WELLS BROWN, _Page_ ix-xxix"
print(upper_vowels(t1))
print(upper_vowels(t2))
print(upper_vowels(t3))
# NONONONONONONONONNONO to below
# print(upper_vowels(t1, t2, t3)) # will give an error

####

# using .split() and the in keyword

# when given a string, in checks for substring membership
print("hell" in "hello") # True

different_text = "here's some different text yaaaay"
print("rent" in different_text) # True
# maybe this isn't what I wanted
# we can use `in` in a more restrictive way with a list
words = different_text.split() # use the split method to break it into a list
print(words)
# when `in` is given a list it checks for EXACT matching membership
print("rent" in words) # False
print("yaaaay" in words) # True, must be an exact match member of the list
print("yaaaa" in words) # False


