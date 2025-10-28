text = "here's some text to work with"
# doing a basic counter pattern
e_count = 0
i_count = 0
u_count = 0
# loop over the source data
for character in text:
    if character == "e": # a filter
        e_count = e_count + 1
    elif character == "i":
        i_count = i_count + 1
    elif character == "u":
        u_count = u_count + 1

# print(e_count, i_count, u_count)

# we don't want to explicitly encode all these things
# let's make a structure to automatically adjust

# when we have an unknown number of things to measure
# dict accumulator pattern without prepopulation
text = "here's some text to work with"

counts = {} # {character: count}
# in keyword works for dict, checks key membership
for character in text:
    # we need to have a structure that detects if something
    # is in the dict or not
    if (character in counts) == False: # if key not in dict, dict[key] = value
        counts[character] = 1
    else:
        # counts[character] = counts[character] + 1
        counts[character] += 1 # the same as above
print(counts)

# doing the logic the other way around
counts = {}

for character in text:
    if character in counts: # if we have it, increment
        counts[character] += 1
    else: # otherwise, create
        counts[character] = 1

# using the dict.get method
counts= {}
for character in text:
    counts[character] = counts.get(character, 0) + 1

print(counts)

# let's get some content out of here
print(counts['x'])
print(counts[" "])
print(counts["'"])
# print(counts['z']) # key error