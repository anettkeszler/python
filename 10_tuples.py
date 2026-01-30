# TUPLES

# declare an empty tuple:
empty_tuple = ()

# tuple can hold any data types
mixed_tuple = (1, "a", 3.14, True)


# access values is possible based on index
print(mixed_tuple[1])       # "a"
print(type(mixed_tuple))    # <class 'tuple'>


# tuple.count() - count the occurance of a value
print(mixed_tuple.count("b"))       # 0, 'b' is not in the tuple
print(mixed_tuple.count("a"))       # 1

# tuple.index() - get the index of given value
print(mixed_tuple.index(3.14))      # 2


# iterate over tuple
for x in mixed_tuple:
    print(x)