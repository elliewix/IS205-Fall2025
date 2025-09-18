# we know a function is one when it is
# name()

# we can use it empty
print()
# you can give it one argument
print("hello for 7")
# you can give it multiple args
print("hello", "world", "9")
# print can use a varible amount of args
# but not all functions can
# let's look at round()
# print(round()) # not designed to be empty
print(round(14.2))
print(round(14.7))
# you can also give it multiple
print(round(16.7786568, 2))

# when you use a function with ()
# you are "calling" it
# "calling it to action"
print(print) # not asking it to do anything
print(round)
# vs calling it
print(round(24.9)) # this is calling
print(round(26.0000))
print(26 % 10)
print()

#### importing functions
# let's import the math module
# commenting out so the later sections work
# import math
# print(math.sqrt(9)) # this is a function
# print(math.pi) # this is a value we can use

# import math as maths # import as an alias
# print(maths.pi)
# print(maths.sqrt(9))

# don't actually use this but this
# is how another thing works
# not for general use
from math import *
print(sqrt(9))
print(pi, e)

#####
# let's talk about defining functions
# this defines the function
def say_hello(name):
    # do our business
    greeting = "hello there, " + name
    return greeting
# now we need to call it
print(say_hello("Elizabeth"))