# infile to read in the updatedtext.txt file


infile = open('updatedtext.txt', 'rt', encoding='utf-8')
text = infile.read()
infile.close()

# say we want some words out of this string

print(text)
# get the words out of this string
# just use .split() and don't worry further
words = text.split()
print(words)

for w in words: # w is fine, w for "word"
    # print(w, len(w), w.upper())
    # what if we want to only see the words of length 6
    # or longer? we want to use a filter pattern
    if len(w) >= 7: # if this is true.....
        print(w)

## changing things up

print("here's the text again....")
# print(infile.read()) # I can't reread, because the file is closed

# if we want to reread things again in a diff way
# we need to do infile again
# for this, we'll look at readlines()
infile = open('updatedtext.txt', 'rt', encoding='utf-8')
# use the lines variable when you get a list of lines
lines = infile.readlines() # use this if you want lines
infile.close()
print(lines)

# if you use readlines, the newlines (\n) will be retained

# however, you can also use another string pattern....
infile = open('updatedtext.txt', 'rt', encoding='utf-8')
text = infile.read()
infile.close()
# splitlines
lines = text.splitlines()
print(lines)
