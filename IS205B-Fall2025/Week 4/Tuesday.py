"""
Essential function def template:

def function_name(param1, param2, etc...):
    # you do your business in here
    # whatever that function is supposed to do
    # determine result
    return result

Four questions before writing a function:
1. What is the function name?
2. What should the parameters or inputs be?
3. What business should it complete?
4. What should it return?
"""
from distutils.dep_util import newer

"""
For the func from thursday...
1. say_hello
2. a name, as a string
3. construct a greeting with a name
4. return the greeting, which is a string
"""

"""
1. call it find_x
2. it should take in a word to check, input_word
3. it should check if the letter x in inside input_word
    don't care if upper or lower
4. it should return True or False, as a boolean
"""

# playing with the concept of 3 first
# let's talk about the "in" keyword
# operator that checks for membership

print("x" in "some text") #True
# checks substrings when given str on right
print("x" in "EXTRA") #oops False

word = "EXTRA"
lowered_word = word.lower()
print(lowered_word)
print("x" in lowered_word) # True
print("ext" in lowered_word) # True

"""
1. call it find_x
2. it should take in a word to check, input_word
3. it should check if the letter x in inside input_word
    don't care if upper or lower
4. it should return True or False, as a boolean
"""
print("now writing our function")
def find_x(input_word):
    lowered = input_word.lower()
    result = "x" in lowered
    return result

print(find_x("extra")) # True
print(find_x("EXTRA")) # True
print(find_x("cat")) # False