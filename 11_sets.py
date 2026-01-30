# SETS

empty_set = {}

my_set = {1, 2, 3, 4, 5, 5}
print(my_set)               # {1, 2, 3, 4, 5} no duplication

# add items to the set
my_set.add(6)       # will be added to the end
print(my_set)

# remove() - remove item from the set
my_set.remove(2)    # number 2 will be removed

# discard() - does the same as remove
my_set.discard(3)   # number 3 will be removed

print(my_set)       # {1, 4, 5, 6}


# MATHEMATICAL OPERATIONS ON SET
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}


# union or | -  joins 2 sets without duplications
print(set1.union(set2))         # {1, 2, 3, 4, 5, 6, 7, 8}

# intersecion or & - give back values which occures in both sets
print(set1.intersection(set2))  # {4, 5}

# difference or '-' - get back all the elements that are only in set1, and not in set2
print(set1.difference(set2))    # {1, 2, 3}

# Symmetrical difference or ^ - get back all the elements that are present in set_a or set_b, but not in both sets
print(set1.symmetric_difference(set2))  # {1, 2, 3, 6, 7, 8}


