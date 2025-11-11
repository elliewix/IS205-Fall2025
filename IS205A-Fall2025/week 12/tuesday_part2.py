import json

infile = open('results.json', 'rt', encoding='utf-8')
data = json.load(infile)
infile.close()

print(data)

print(data['a']['lines'])
print(data['e']['count'])

all_matches = 0

for vowel, d in data.items():
    count = d['count']
    all_matches += count
print(all_matches)