for letter in "abc":
    print(letter)

for num in [1,2,3]:
    print(num)

# we can nest these to see the combinations
for letter in "abc": # this is the outer loop
    for num in [1,2,3]: # our inner loop
        print(letter, num)
        # print(num, letter)

for num in [1,2,3]:
    for letter in "abc":
        print(letter, num)

### writing out files from a loop
# hint: what we'll see here will become the outer loop

terms = ['cat', 'dog', 'house']
# these terms will become their own files...
# start by looping over the terms
for t in terms:
    # always check your file names first
    print(t + ".txt") # we want term.txt

# print(500000 ** 4)

####
terms = ['rabbit', 'horse']
# outfile pattern within a for loop
for t in terms:
    filename = t + ".txt" # once this looks good, you can make the file
    outfile = open(filename, 'wt', encoding='utf-8')
    # our filename is now a variable
    # presumes I have one string to write out
    outfile.write("The term was   " + t) # write out your content
    outfile.close()

# but what if I have more things to write out??

"""
if we're going after....

outer loop of the file names or content that makes file names....
    open your file
    inner loop creating the content
        writing that content to the file
    close the file
"""

# let's see an example
# for the sake of the example, we'll use a loop but
# do something a bit silly

terms = ['cat', 'dog', 'house']

for t in terms:
    filename = t + ".txt"
    # print(filename) # always check your filename first
    outfile = open(filename, 'wt', encoding='utf-8')
    # working between the open and close....
    for char in t:
        outfile.write("A letter is " + char + '\n')
    outfile.close()


