"""
our basic function def syntax:

def function_name(param1, param2, etc.):
    # this is the area where the func does stuff
    # so do your business with param1 etc.
    # determine your result
    return your_result

Answer these questions before any code:
1. What is the function name?
2. What inputs/params should it take?
3. What business should it to? or actions?
4. What should it return?

"""

"""
for the function we did thursday
1. What is the function name? 
    say_hello
2. What inputs/params should it take?
    always note the data type for yourself
    name, will be a string
3. What business should it to? or actions?
    constructs a greeting and returns it
4. What should it return?
    the greeting string

"""

"""
let's write a new one today
1. What is the function name? 
    find_x
2. What inputs/params should it take?
    a single string of text
3. What business should it to? or actions?
    determine if the letter x is in the string
    upper and lowercase are to be found
    don't need to do anything diff if multiple
4. What should it return?
    True or False, as booleans
    
Prior experience: go ahead and start developing
Beginners: consider working on step 3 seperately 
"""

# work on step 3 separately then put together as
# a function

text = "EXTRA: here's some text" # Expect True for this
lowercased_text = text.lower() # lowercase the text
# use as an operator for checking membership
# return back True or False
# caution! will work differently for data types
# strings: checks substrings
print("x" in lowercased_text) # True
print("x" in "hello") # False
print("x" in "EXTRA") # False
# but if I say alone
"x" in "cat" # will be evaluated but nothing printed

#### review the stuff above when writing our function

"""
1. What is the function name? 
    find_x
2. What inputs/params should it take?
    a single string of text, called input_text
3. What business should it to? or actions?
    determine if the letter x is in the string
    upper and lowercase are to be found
    don't need to do anything diff if multiple
4. What should it return?
    True or False, as booleans
"""
print("begin writing and testing function")
def find_x(input_text):
    # doing our business
    lower_text = input_text.lower()
    result = "x" in lower_text
    return result
# in order for our function to work, we need to call it
# calling it three times to check our diff items
print(find_x("extra")) #True
print(find_x("EXTRA")) # True
print(find_x("cat")) # False

# let's expand on this

"""
What if I changed my mind and I wanted to expand this function def
to accept the string to check and the letter to find?
1. prob need to change the name: find_letter
2. add a new input: the letter to find
3. replace usage of "x" with the variable from parameters
4. return doesn't change
"""

def find_letter(input_text, letter):
    # doing our business
    lower_text = input_text.lower()
    result = letter in lower_text
    return result

# call my updated function
print("my updated function")
print(find_letter("extra", "x"))
print(find_letter("cat", "c"))
# so this tech works, but not my intent
print(find_letter("elizabeth", "liz"))
