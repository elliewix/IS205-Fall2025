
# practice list methods and accum patterns without dicts

empty_list_for_stuff = []
for num in [5, 8, 9]:
    empty_list_for_stuff.append(num)

    print(empty_list_for_stuff)

## let's make a dict and play with that

data = {}
# key: 'a', value: [], how do I add these things into my dict?
data['a'] = []
print(data)
# let's add just something into that list to see it
# use dict[key] like a variable for that value
data['a'].append("hello there")
print(data)

# let's start doing some real stuff

# write a detection function to check if the line
# is what we want
def detect_line(line): # takes in a line
    line = line.lower() # lower cases it
    if line.startswith('a') == True: # checks the start
        return True # if we have a positive match
    else:
        return False

# now let's loop over data

infile = open('europe_snippet.txt', 'rt', encoding='utf-8')
# infile = open('Three-years-in-europe.txt', 'rt', encoding='utf-8')

lines = infile.readlines()
infile.close()

a_lines = [] # collect the lines that start with a
for l in lines:
    # print(detect_line(l)) # check that things are working
    if detect_line(l) == True: # now only print true matches
        a_lines.append(l)# print(l)
# print(a_lines)

# now that we've seen a list accumulator, let's put it in a dict

data = {}
data['a'] = []
for l in lines:
    if detect_line(l) == True:
        # here's our collection point
        data['a'].append(l)

print(data)

# let's see this in a larger context....

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

data = {}
# prepopulate out dict: key: vowel, value: []
for v in vowels:
    data[v] = []
print(data)
for v in vowels:
    for l in lines:
        if detect_line(l):
            data[v].append(l)
            # .....  and now we realize there's a problem

print(data['e'])
#..... oops let's update that function

def match_a_line(line, letter):
    line = line.lower()
    letter = letter.lower()
    if line.startswith(letter):
        return True
    else:
        return False

data = {}
# prepopulate out dict: key: vowel, value: []
for v in vowels:
    data[v] = []
print(data)
for v in vowels:
    for l in lines:
        if match_a_line(l, v):
            data[v].append(l)

print(data)

# we can loop over it to see the content better...
print(data)
for key, value in data.items():
    print(key, value)
print(data.items())
for l in lines:
    if match_a_line(l, "this"):
        print(l)

for pair in data.items():
    print(pair)

##
# I could do this in a shorthand...

results = [l for l in lines if detect_line(l)]
print(results)
dict_results = {v: [l for l in lines if match_a_line(l, v)]
                    for v in vowels}
print(dict_results)

