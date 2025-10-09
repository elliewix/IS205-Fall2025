# ignore my regrets and just use pycharm like normal

# some stuff that we've done before....
# read in the file and clean up the words

infile = open('longestsentence.txt', 'rt', encoding = 'utf-8')
text = infile.read()
infile.close()
#  let's do a little bit of cleaning before we get going....
# this isn't related to hw3 though
text = text.replace('—', ' ') # corrects the em dash
text = text.replace('-', ' ') # corrects the en dash

# print(text)
words = text.split()
print(len(words))

# print(words)

# let's clean up the words
import string
cleaned = [] # creating the base of my list accumulator
for w in words:
    w = w.lower()
    w = w.strip(string.punctuation)
    # print(w)
    cleaned.append(w) # no assignment statement
print(cleaned) # note the indent here, outside of and after my loop

# let's print out "long" words of length 9 or more
# and count how many there are...

count = 0 # creating the base of my integer accumulator
for w in cleaned:
    if len(w) >= 9:
        # print(w)
        count = count + 1  # count += 1 does the same thing

print(count) # note the indent and placement here to see the final result

# now let's write this content out to a file
# I could add this into my previous for loop, but I don't wanna

outfile = open('longwords.txt', 'wt', encoding='utf-8') # base for file accumulator
for w in cleaned:
    if len(w) >= 9:
        outfile.write(w + '\n') # you may need to add a newline character
        # outfile.write(w) # use this one if you don't need to add the newline
outfile.close() # !! important, note the indent and placement here
# close your file at the same indent level as you created it

## one last thing to explore.....
# putting text back together once you've collected it from a list
# we want to put all the words in cleaned back into a single string
# with a single space between each
rejoined = " ".join(cleaned)
# call join on the delimiter and pass it the sequence to connect
print(rejoined)
