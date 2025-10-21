for letter in "abc":
    print(letter)

for num in [1, 2, 3]:
    print(num)

# a nested loop to see everything

for letter in "abc":
    for num in [1,2,3]:
        # print(letter, num)
        print(num, letter)

# before we are writing out with a nested loop
# we need to write out files in a loop to start

# the examples below are mostly about what will
# become the outer loop

terms = ['cat', 'dog', 'horse']

for t in terms:
    # the term needs to become the filename
    print(t + '.txt') # our pattern should be term.txt

# print(500000 ** 4)

### now that we can make file names, we can write things out

terms = ['cat', 'dog']

for t in terms:
    filename = t + ".txt"
    outfile = open(filename, 'wt', encoding='utf-8')
    # in the middle is where I put the content
    outfile.write("The term was " + t)
    outfile.close()

# adding more content to the inside of the files

terms = ['cat', 'dog', 'horse']

for t in terms:
    filename = t + ".txt"
    outfile = open(filename, 'wt', encoding='utf-8')
    # let's do a silly example but it'll show an inner loop
    for char in t:
        outfile.write("A letter is " + char + "\n")
    outfile.close()