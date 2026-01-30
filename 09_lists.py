# LISTS

# declare an empty list
my_empty_list = []

# list of integers
nums = [1, 2, 3, 4, 5]

# list of strings
list_of_strings = ["a", "b", "c", "d"]

# list of different data types
list_of_mix = [1, "A", 3.14, True, (1, 2)]

# nested list 
nested_list = [1, 2, 3, [4, 5, 6]]


# LIST METHODS
numbers = [1, 2, 3, 4]

# insert() - list.insert(index, value)
numbers.insert(2, 3)
print(numbers)

# append() - puts the value at the end of te list, no need to specify the index 
numbers.append(7)
print(numbers)

# extend adds another list to the end the original list
numbers.extend([8, 9, 10])
print(numbers)

# remove items from the list:
numbers.remove(3)
print(numbers)

# pop(index)
numbers.pop(0)      # removes the first item from the list, at index zero
print(numbers)

numbers.pop(len(numbers)-1)     # removes the last item from the list
print(numbers)

# del keyword
del numbers[0]      # deletes the first itrem in the list, at zero index
print(numbers)

# LIST INDEXING:
fruits = ["apple", "banana", "orange"]
fruits[0]               # "apple"
fruits[-1]              # "orange"
"banana" in fruits      # True
len(fruits)             # 3


