# when we work with dictionaries, we aren't working
# with positions
# dicts are our key/value pair structure
# key: value
# keys must unique within a dict
my_data = {'a': 10, 'b': 5}
# keys should always be strings
# values can be anything but have a patten
# or rules (schema) about it
# we access stuff via keys
print(my_data['a'])
# accessing it gives the actual value
print(my_data['b'] + 7) # you can act on it
# like you would the actual value
# the key must match exactly
# print(my_data['A']) # error

# want to add a new key/value pair
# use assignment syntax
# we want add 'c': 15 (key: value), dict[key] = value
my_data['c'] = 15
print(my_data)

# update syntax
my_data['b'] = 20
print(my_data)

# looping over dictionaries

for key, value in my_data.items():
    print(key, value)

for letter, count in my_data.items():
    print(letter, count)

# creating a dict from a list of keys
# dict accumulator pattern

vowels = ['a', 'e', 'i', 'o', 'u']
data = {} # empty dict
# add each letter with a value of 0
for v in vowels:
    # print(v) # v will be our key
    data[v] = 0
print(data)