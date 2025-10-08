# changing the cleaning pattern from replace to strip
# replace works on string.replace(old, new)

# string.strip() works diff
# strip takes many options
# looks inside the string for any instances
# but only of the ones I gave it
print("cats!!!! cats!!!! cats!!!!".replace("!", ""))
print("cats?!?!?! cats?!??!!! cats!!!!".replace("!", ""))
# you can provide more than one character
print("cats?!?!?! cats?!??!!! cats!!!!".replace("cats", ""))
# but that will only be looking for full matches to remove
print("cats?!?!?! cats?!??!!! cats!!!!".replace("stac", ""))


print("now playing with strip....")
# strip works diff in 2 ways
# you still call it on a string, but it only looks
# to the outside, stops looking as soon as a nonmatch appears
print("cats?!?!?! cats?!??!!! cats!!!!".strip("!"))
# strip checks from both sides
# the weirder thing it does.... it treats each character
# as a possible thing to remove
print("!?!?!??!$$@#!!!cats?!?!?! cats?!??!!! cats!!+??!!".strip("!"))
print("!?!?!??!$$@#!!!cats?!?!?! cats?!??!!! cats!!+??!!".strip("!?"))
# the order doesn't matter because again, each character is considered
print("!?!?!??!$$@#!!!cats?!?!?! cats?!??!!! cats!!+??!!".strip("?!"))

# strip in more natural environments
# for us, we'll be giving it string.punctuation
import string
print(string.punctuation)
print("--don't?!!".strip(string.punctuation))

print("---'Wait, the *cats* __don't__ like the food???!!!".strip(string.punctuation))

sen = "---'Wait, the *cats* __don't__ like the food-food???!!!"
words = sen.split()
for w in words:
    print(w.strip(string.punctuation))

###
print("and now for a list accumulator pattern")

sen = "---'Wait, the *cats* __don't__ like the food-food???!!!"
words = sen.split()
cleaned = [] # outside of and before my for loop
for w in words:
    clean_word = w.strip(string.punctuation)
    cleaned.append(clean_word) # puts the word into the list
    # append is a mutating method! no assignment statement
    # if you start getting NoneType errors, you likely have
    # an assignment somewhere you shouldn't
print(cleaned) # note the indent here, OUTSIDE OF MY FOR LOOP

####

l = [5,8,6,5,7,9,0,7]
l.sort() # how you should do it
print(l)

# however
l = [5,8,6,5,7,9,0,7]
l = l.sort() # how you should do it
print(l) #oops, now I see none???
# print(l[0]) # will give you an error

l = [5,8,6,5,7,9,0,7]
print(l.sort())
print(l)

# None() # you tried to call it like a function
print(l[1]) # I wanted this.....
# but I said
# print(l(1)) # will generate a not callable error

