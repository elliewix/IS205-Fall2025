# practice and review some core syntax for things

my_list = []
my_list.append('some stuff')
my_list.append('more stuff')
print(my_list)

# list accumulator pattern
my_stuff = []
for num in [1,90,8,9]:
    my_stuff.append(num)
print(my_stuff)

# review a bit of dict stuff
data = {}
# add a key and value
# data[key] = value
# add 'a' as a key with [] as value
data['a'] = []
print(data)
# let's add something to that list....
data['a'].append("hello there")
print(data)

## work on our actual data

infile = open('europe_snippet.txt', 'rt', encoding='utf-8')
lines = infile.readlines()
infile.close()
print(lines)

def detect_line(line):
    line = line.lower()
    if line.startswith('a') == True:
        return True
    else:
        return False

a_lines = []
for l in lines:
    # print(detect_line(l))
    if detect_line(l) == True:
        a_lines.append(l) # print(l)
print(a_lines)

#### what if we had a dict?

vowel_dict = {}
vowel_dict['a'] = []

for l in lines:
    # print(detect_line(l))
    if detect_line(l) == True:
        vowel_dict['a'].append(l) # print(l)
print(vowel_dict)

## say we want to do this for all vowels

def match_a_line(line, letter):
    line = line.lower()
    letter = letter.lower()
    if line.startswith(letter):
        return True
    else:
        return False

vowels = ['a','e','i','o','u', 'y']
vowel_data = {}

for v in vowels:
    vowel_data[v] = []
print(vowel_data)

for v in vowels:
    for l in lines:
        if match_a_line(l,v):
            vowel_data[v].append(l)

print(vowel_data)

# fun fact example time

a_matches = [l for l in lines if detect_line(l)]
print(a_matches)
# {key: value for loop.....}
vowel_matches = {v: [l for l in lines if match_a_line(l, v)] for v in vowels}
print(vowel_matches)