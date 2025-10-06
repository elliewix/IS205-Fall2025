# classic infile pattern

# 1- tell python about the file
infile = open('cats.ihatezoom', 'rt', encoding='utf-8')
# 2- tell python what to do with it (.read())
# 3- where save the contents (text)
text = infile.read() # "read" from top to bottom return as str
# tell python to "unlock" the file
infile.close()
# 4- get to business on it
print(text) # this is just a python string

sentence = "here's some extra text and things"
sentence = text + sentence
print(sentence)
# now that we have content we can write this file out
# this is the outfile pattern
# outfile = open('cats.unicornfuzzies', 'wt', encoding='utf-8')
outfile = open('updatedtext.txt', 'wt', encoding='utf-8')
# now I can use the writing methods to put content in
outfile.write(sentence) # note no assignment
outfile.close()