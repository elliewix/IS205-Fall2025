# replace vs strip
# replace takes old, new and replaces single instances
import string

print("hello!!!".replace("!", ""))
print("cats!!! cats!!! cats!!!!".replace("!", ""))

text = "cats!!! cats!!! cats!!!!"
print(text.replace("cats", ""))
print(text.replace("stac", "")) # won't work

print("strip works differently")
# it will only remove characters from the "outside"
print(text.strip("!"))
# it also treats individual characters as separate units
# to remove
text2 = "!!!!!+!!!What? The *cats* __don't__ like their food-food??!!++?"
print(text2.strip("!+?"))

words = text2.split()
print(words)
import string
print(string.punctuation)
cleaned = [] # before and outside of my loop
for w in words:
    clean_word = w.strip(string.punctuation)
    cleaned.append(clean_word) # no assignment!
print(cleaned) # outside of and after, pay attention to the indent

# example errors

l = [8,67,65,789,9,9,5,3,1,0,8,9,87]
l.sort() # how you should do it
print(l)
# however, there are some very easy/honest mistakes you can make

l = [8,67,65,789,9,9,5,3,1,0,8,9,87]
l = l.sort()
print(l)
# print(l[0])
# you may also see this error...
# print(l(1))

l = [8,67,65,789,9,9,5,3,1,0,8,9,87]
print(l.sort())
print(l)