# let's talk about functions in general
# we know we have a function when
# name()
print() # sometimes they work empty
# or one argument
print("hello")
# some can take many
print("hello", "there")
print("hi", "fellow", "human", "number", 9)

# let's look at round
# print(round()) # has no empty definition
print(round(13.4)) # you can use one number
# also give it an optional arg
print(round(15.4589, 2))

# function calling
# when you ask the function to execute
# the () are required
# here's some cursed looking code
print(round)
print(print)
# you likely forgot the () if you see these

####
# importing modules

import math
print(math.sqrt(9))

# alternatively you can give it an alias
import math as maths
print(maths.sqrt(9))

###
# defining custom functions

def say_hello(name):
    greeting = "hello there, " + name
    return greeting

print(say_hello("Elizabeth"))