text = "here's some text to work with"
e_count = 0
a_count = 0
i_count = 0
for character in text:
    if character == "e":
        e_count = e_count + 1
    elif character == "a":
        a_count = a_count + 1
    elif character == "i":
        i_count = i_count + 1

print(e_count, a_count, i_count)

# what if we had an unknown number of possible keys?
# we are going to use a dictionary accumulator pattern
# not going to prepopulate

text = "here's some text to work with"
counts = {}
for character in text:
    if (character in counts) == False: # our first time seeing, not in there yet
        counts[character] = 1
    else: # already in there, we need to add 1
        # counts[character] = counts[character] + 1
        counts[character] += 1 # these are the same
print(counts)

## flipping the logic around

counts = {}
for character in text:
    if character in counts: # we seen it already
        counts[character] += 1
    else: # not seen it yet
        counts[character] = 1
print(counts)

# using the dict.get() structure

counts = {}
for character in text:
    counts[character] = counts.get(character, 0) + 1
print(counts)

### looking things up from a dictionary

print(counts['x'])
print(counts['\''])
print(counts["'"])
print(counts[" "])
# print(counts['z']) # key error
print(counts.get('z', 0)) # will give me 0