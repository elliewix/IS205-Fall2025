# repeating the infile thing
infile = open('updatedtext.txt', 'rt', encoding='utf-8')
text = infile.read()
infile.close()

print(text)
# say we want the words out of this text
words = text.split()
print(words)
for w in words: # w for "word" here
    # print(w, len(w))
    if len(w) >= 7: # if this is true...
        print(w)

# let's look at how we can read things in a bit diff
# say we wanted to load the file as lines right away...

infile = open('updatedtext.txt', 'rt', encoding='utf-8')
lines = infile.readlines()
infile.close()
print(lines)

# if you want lines but still use .read()
infile = open('updatedtext.txt', 'rt', encoding='utf-8')
text = infile.read()
infile.close()

lines = text.splitlines() # a string method that splits lines...
print(lines)