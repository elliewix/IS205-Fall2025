text = "hello here are some words, this is text ple,ase enjoy it"

words = text.split()
# loop through the words and count the letters
# position = 0
# for w in words:
#     print(position, w, len(w))
#     position += 1
#

# for w in enumerate(words):
#     pos = w[0]
#     word = w[1]
#     print(pos, len(word), word)

# now we have the base of the rows we want to write out

# collect the data rows in a 2D list
rows = []
for w in enumerate(words):
    pos = w[0]
    word = w[1]
    # print(pos, len(word), word)
    r = [pos, len(word), word] # make it into a list
    rows.append(r) # adds the row into the collection list

print(rows)
# we have our 2D list of rows, but we need headers
headers = ['position', 'word length', 'word'] # each col name as string

# now we have a 1D list of headers and our 2D list of data
# ONLY at this point are we ready to write the csv out

import csv
outfile = open('wordcounts.csv', 'wt', encoding='utf-8')
csvout = csv.writer(outfile)
# write the headers
csvout.writerow(headers) # use singular with 1D row
csvout.writerows(rows) # use plural with 2D rows
outfile.close()
# DO NOT use .join() or other concatenation method to create the rows for the text file

# okay for the curious here's how we do it in 305

import csv
with open('wordcounts.csv','rt', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

with open('wordcounts_2.csv', 'wt', encoding='utf-8') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(headers)
    csvout.writerows(data)

with open('wordcounts_2.csv', 'wt', encoding='utf-8') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(headers)
    csvout.writerows(data)