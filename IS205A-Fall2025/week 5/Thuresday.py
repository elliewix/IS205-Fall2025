# define 2 functions
# hello(name) will produce a greeting
# format_name(name) will format a name
# hello will use format_name to correctly
# format the name before creating the greeting

# effectively
# functionA and functionB,
# functionB will use functionA

def format_name(name):
    # title case whatever comes in
    # don't actually use this in real life
    formatted = name.title()
    return formatted

def hello(name):
    greeting = "hello " + format_name(name)
    return greeting

print(format_name("ELIZABTEH WICKES"))
print(hello("ELIZABETH WICKES AND FRIENDS"))