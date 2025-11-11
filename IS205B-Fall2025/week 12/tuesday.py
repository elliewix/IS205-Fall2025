def match_a_line(line, letter):
    line = line.lower()
    letter = letter.lower()
    if line.startswith(letter):
        return True
    else:
        return False

## let's explore the syntax here

data = {}

data['a'] = {'count': 0, 'lines': []}
print(data)
print(data['a'])
print(data['a']['lines'])
data['a']['lines'].append("apples")
print(data)
data['a']['count'] += 1
print(data)

## let's see what prepopulation looks like here

vowels = ['a', 'e', 'i','o','u', 'ee']
data = {}

for v in vowels:
    data[v] = {'count': 0, 'lines': []}
print(data)

# now we have our structure, let's go into our data

infile = open('europe_snippet.txt', 'rt', encoding='utf-8')
lines = infile.readlines()
infile.close()

for v in vowels:
    for l in lines:
        if match_a_line(l, v):
            data[v]['lines'].append(l)
            data[v]['count'] += 1
print(data)

# dump this out as a json file

import json

outfile = open('results.json', 'wt', encoding='utf-8')
json.dump(data, outfile, indent = 4)
outfile.close()