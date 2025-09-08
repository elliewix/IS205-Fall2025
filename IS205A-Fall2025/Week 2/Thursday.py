print(1)
print("2")
print(3.0)
print("4.5")

######
# operators
my_number = 8 # assignment operator
print(my_number)

# + operator
print(10 + 2) # int + int does addition
print("1" + "3") # str + str does concatenation
# data types on both sides need to "match", sort of
# things that will generate errors
# print(1 + "6") # unsupported data types
# a few ways to fix this
# most of the time you wanted the number to be a string
# you can "recast" the number to a string with str()

# print(21 + " bananas") # error because int + str
# we need to recast it to be a string
print(str(23) + " bananas")
# why didn't I just use quotes to fix this?
num_bananas = 25
print("num_bananas") # nope, that's just a string
# print(num_bananas + " bananas") # error, int + str
print(str(num_bananas) + " bananas")

# can you go the other way?

print(int("30") + 2) # if we really wanted math
# print(int("30.5") + 3) # wait what do I mean?
print(int(float("30.5")) + 4) # we don't do this that much

#####
# boolean values
print(True)
print(False)
# print(true)

i = "here's some text" # no
# these would be okay
# text, my_text, sentence, sen, in pinch: s

