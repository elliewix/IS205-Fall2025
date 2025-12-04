text = "here's some text for you, ple,ase enjoy it all"
#
# words = text.split()
# position = 0
# for w in words:
#     print(position, len(w), w)
#     position += 1

# these are the things that we want, now we want to make
# them into a CSV file

words = text.split()
position = 0
rows = []
for w in words:
    r = [position, len(w), w] # make a row of data
    rows.append(r) # collect the row
    position += 1
print(rows) # now we have a 2D list of data/rows
headers = ['postion', 'word length', 'word'] # create out 1D headers list
# only now that we have a 1D headers list and a 2D row list
# should we attempt to write out the CSV file

import csv
outfile = open('wordcounts.csv', 'wt', encoding='utf-8')
csvout = csv.writer(outfile)

csvout.writerow(headers) # singular for 1D list, your headers
csvout.writerows(rows) # plural for 2D list, your data
outfile.close()

# DO NOT USE ",".join() or any other string concat for
# creating the rows and writing them out
# you will get a 0 the CSV element