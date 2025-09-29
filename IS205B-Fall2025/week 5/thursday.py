# we're going to define two functions
# one that calls the other

# format_name(name) will title case a string
# hello(name) will generate a greeting
# hello will use format_name

def format_name(name):
    # don't actually treat names like this
    formatted = name.title()
    return formatted

def hello(name):
    greeting = "hello there " + format_name(name)
    return greeting

print(format_name("ELIZABETH WICKES"))
print(hello("ELIZABETH WICKES AND FRIENDS"))