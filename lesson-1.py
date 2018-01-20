
### Basic output
print('hello banana')  # Cause text to appear in the console

### Variables

# Values can be stored in variables for later use
a = 8
# After this, print(8) and print(a) would produce the same behavior

### Data types

## Aside from numbers, there are different 'data types' in python

## Simple types
a = 10  # number
a = 12.43  # number
a = "banana"  # string
a = True  # boolean
a = False  # boolean

## Composite types (containers that contain simple/composite types inside them)

# List

# A list is an ordered sequence of values
a = ["apple", "banana", "grape", "durian"]
# The values in the list do not have to be of the same type
a = ["apple", "banana", 5, 4, True]
# The values may include composite types
a = ["apple", ["one", "two", [3, 4]]]

# Accessing values in a list
# Use listName[i] to access the i-th item of the list (remember that we start a 0!)
seasons = ['winter', 'spring', 'summer', 'fall']
print(seasons[2])  # prints 'summer'

randomThings = ['banana', [1, 4, False], 'grape']
print(randomThings[1])  # prints [1, 4, False]
print(randomThings[1][2])  # prints False

# Tuple

# similar to a list, but uses () instead of []:
myTuple = (1, 3, 5, 7)

# use tuples when
# a) all the values have the same type
# b) you don't plan to modify the tuple


# Dictionary

# A dictionary, like a List, contains other values inside of it
# In a dictionary however, the values you place inside of it are given labels
# The syntax of a dictionary is {} braces, with label/value pairs (label: value) inside
# and commas between the label/value pairs
a = {
    'bananaCount': 3,
    'appleCount': 5,
    'grapeCount': 7
}

# Since we've given our values labels, we can access them by name, rather than by position as in a List

print(a['grapeCount'])  # prints 7

# If we had used a List instead
a = [3, 5, 7]

# Then it's difficult to understand the context of what those values mean, since they are not labeled


### Flow Control

## if and if/else
banana = 5

# Use the 'if' keyword to execute a block of code IF some condition is true
if banana >= 5:
    # This block will get executed if banana is greater than or equal to 5
    print('goat')
    print('apple!')

# Use 'else' to execute a block if the first condition is NOT met
mango = 43
if mango > 45:
    print('huge mango')
else:
    print('tiny mango')

# Between if and else, you may use any number of 'elifs'
# Python will check each condition, and execute the block under the first true condition
# If no conditions are found to be true, the else block will be executed
lychee = 67
if lychee > 89:
    print('huge')
elif lychee > 64:
    print('medium')
else:
    print('large')


## Loops

# A loop is a way to execute a block of code N number of times

for i in range(100):
    # Will get printed 100 times:
    print('bananaman')
    # the variable i stands for the current repetition we're on
    # so the first time this block executes, i = 0. next time, i = 1, etc, up until 99
    print(i)



### Built-in operators

# Pretty much what you'd expect, with a few new faces

a = 1 + 2
a = 1 - 2
a = 1 / 2
a = 1 * 2
a = 1 ** 2  # exponentiation
a = 9 % 5  # modulus ("clock" operator)


### Functions

## A function is a block of code that can be executed at some later time or later time(s)
## In many styles of programming, they are the primary way to organize code
## Using functions allows us to avoid repeating code, and write clearer code

# Functions can "do things" (make stuff happen) and/or compute and "return" a value

# Use the 'def' keyword, followed by the name of the function, followed by the argument list
# We'll start with a function with no arguments
def print_some_stuff():
    print("some stuff")
    print("some more stuff")
    print("done")

# Executing the above code will cause no visible output: remember that defining a function is only
# defining a block of code that will be executed later. It's like writing down a recipe, not baking a cake

# To bake the cake (make the function run), we need to "call" the function, which looks like this:
print_some_stuff()

# When the above line executes, python will jump into your print_some_stuff function, and execute the code
# inside of it (i.e. print those three lines)

# Arguments (sometimes called args) provide a way to pass in additional information when calling the function
def print_nice_message(name, gender):
    print("Hello, " + name)
    if gender is 'male':
        print("you are a swell guy")
    elif gender is 'female':
        print("you are a swell gal")
    else:
        print("you are a swell.. one")

# This makes the function more flexible. It can now be called with different arguments to produce different behavior
print_nice_message('Jackmerius Tacktheritrix', 'male')
print_nice_message('LaCarpetron Dookmariot', 'female')

# The first call will print a nice message to Jackmerius
# The second call will print a nice message to LaCarpetron

# BTW, the following line would produce an error, since we defined our function to expect 2 args
print_nice_message("Hingle McCringleberry")


# As mentioned, in addition to receiving args, a function can also RETURN a value
# Functions that do both of those things are getting closer to a formal math-y function
def double(x):
    return x * 2

# What does return do? It means to replace the call of the function with the value it returns
# That is,

print(double(10))

# Will be translated into:
print(20)

# Because the function /returned/ 20



### Misc examples

## It's okay if much of this code doesn't make sense to you yet, but I figured I'd give you a few examples
## of how the above building blocks can come together to solve simple problems

# Print the name of the month for a given month number
def print_full_month_name(month_number):
    if (month_number < 1) or (month_number > 12):
        print("Invalid number! Must be between 1 and 12")
        return  # quit the function
    month_names = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november']
    print(month_names[month_number-1])  # we subtract 1 since programmers count from 0 but people count months from 1

# Print the product of two numbers. Catch: no * operator allowed!
def print_product(a, b):
    answer = 0
    for i in range(b):
        answer = answer + a
    print(answer)
