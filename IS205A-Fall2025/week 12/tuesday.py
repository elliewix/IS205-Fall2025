def match_a_line(line, letter):
    line = line.lower()
    letter = letter.lower()
    if line.startswith(letter):
        return True
    else:
        return False

# before we read in data, let's practice syntax

data = {}
data['a'] = {'count': 0, 'lines': []}
print(data)
print(data['a']['lines'])
data['a']['lines'].append('apples')
print(data)
#let's get into count
print(data['a']['count'])
data['a']['count'] += 1
print(data)

## back to prepopulation

vowels = ['a', 'e', 'i', 'o','u', 'ee']
data = {}
for v in vowels:
    data[v] = {'count': 0, 'lines': []}

# get into my data
infile = open('europe_snippet.txt', 'rt', encoding='utf-8')
lines = infile.readlines()
infile.close()

for v in vowels:
    for l in lines:
        if match_a_line(l, v):
            data[v]['lines'].append(l)
            data[v]['count'] += 1
print(data)

# out this data into a json file
import json

outfile = open('results.json','wt', encoding='utf-8')
json.dump(data, outfile, indent = 2)
outfile.close()