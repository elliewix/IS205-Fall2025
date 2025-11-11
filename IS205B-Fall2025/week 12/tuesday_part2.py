import json

infile = open('results.json', 'rt', encoding='utf-8')
data = json.load(infile)
infile.close()

print(data)
# show the lines matching a
print(data['a']['lines'])
# show the counts for e
print(data['e']['count'])
# show the total number of matches
matches = 0
for key in data:
    matches += data[key]['count']

print(matches)