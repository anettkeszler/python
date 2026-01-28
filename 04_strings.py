# STRINGS 

# Use back slash '\' when a line is too long but you want to represent it in a single line 
str = "This is too  \
long for one line  \
so I add a back slash  \
at the end of each line."

print(str)

# Characters in a string can be accessed by its index
name = "John" 
print(name[0])  # J


# Length of the string
print(len(name))    # 4 


# Concatenation
first = "Anett"
second = "Keszler"
print(first + " " + second)


# Multiply with *
repeat = "Meow! " * 3
print(repeat)


# STRING METHODS
print("a".upper())      # "A"
print("A".lower())      # "a"
print("  a ".strip())   # "a" --> remove spaces at the beginning and at the end of the string
print("abc".replace("bc", "ha"))    # "aha"
print("a b".split())    # ["a", "b"] --> splits a string into a list where each word is a list item
print("-".join(["a", "b", "c"]))    # "a-b-c" --> takes all items in an iterable and joins them into one string


# STRING INDEXING AND SLICING
text = "Python"
text[0]         # "P"
text[-1]        # "n" --> last character
text[1:4]       # "yth" --> stop parameter is excluded
text[:3]        # "Pyt" --> from start, stop param excluded (0, 1, 2)
text[3:]        # "hon" --> to end
text[::2]       # "Pto" --> step parameter, every second 
text[::-1]      # "nohtyP" --> reverse

# STRING FORMATTING
name = "Jonathan"
age = 2

# f-string
print(f"Hello, {name}!")
print(f"{name} is {age} years old.")

# format() method
print("Hello, {}!".format(name))
print("{} is {} years old.".format(name, age))