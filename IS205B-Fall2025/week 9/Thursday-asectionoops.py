# previewing dictionaries for next week

# dicts are our key/value pair structure
# we've seen lists, and we access things in them
# by position number
# dicts, you access by key or content
# key: value
my_data = {'a': 10, 'b': 5} # curly braces
# keys: usually going to strings
# values: whatever you need, but do have
# some kind of rules/schema

# now that we've made one.... let's get stuff out of it
# Access: with the key, must be exact: dict[key]
print(my_data['a']) # key is string and must match exactly
print(my_data['b'] + 5) # you can act on the value once you've
                        # looked it up
# note, if I give a key that doesn't exist... error
# print(my_data['A'])

# add a new value into my dict: use assignment statement
my_data['c'] = 9 # will add 'c': 9 into it
print(my_data)

# updating a value:
my_data['b'] = 15
print(my_data)

# looping over a dictionary
for key, value in my_data.items():
    print(key, value)

for letter, count in my_data.items():
    print(letter, count)

# I want to add 5 to all these values

for key, value in my_data.items():
    my_data[key] = value + 5

print(my_data)

## how will you really see dicts in your code?

data = {}
vowels = ['a', 'e', 'i', 'o', 'u']
# prepopulate out dict
# add these keys, set with a base value of 0
for v in vowels:
    # print(v) # the vowel should be the key, 0 is the value
    data[v] = 0

print(data)