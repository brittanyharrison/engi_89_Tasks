"""
The instructions for these activities acan be found on the read
"""
# define a variable `name`, and assign a string
name = "name"
# re assign the original variable with your name
name = "Brittany"

# use concatenation to print a welcome message
# use methods to format the name/input (remove white spaces)
greetings = "Hi " + name + "! Welcome to Sparta Global."
#greetings.strip()
print(greetings.strip())

# Version 2 - with interpolation

# define another variable `full_name` to a random string
full_name = "random string"

while full_name != "quit":
    # re assign the variable `full_name` to a name
    full_name = input("What is your full name?")
    # use interpolation to print the message
    print(f'Hello {full_name.title()}! This is python')


