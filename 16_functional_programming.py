coffees = ["Espresso", "Latte", "Cappuchino", "Macchiato", "Americano", "Decaf"]

def reverse(str):
    return str[::-1]

reversed_coffees = map(reverse, coffees)

for x in reversed_coffees:
    print(x)


# pure function
my_list = [1, 2, 3]

def add_to_list(lst: list, item):
    new_list = lst.copy()
    new_list.append(item)
    return new_list


# it is a pure function, as it doesn't modify the original list (my_list)
new_list = add_to_list(my_list, 4)
print(new_list)

print(my_list)

# Reverse a string 
# 1. slice function - str[::-1]
trial = "reversal"

reverse_trial = trial[::-1]

print(reverse_trial)


# 2. recursion
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]
    
print(string_reverse(trial))

# Map and Filter
menu = ["espresso", "mocha", "latte", "cappuchino", "cortado", "americano"]

# filter menu with all items starting with 'c' 

def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee

map_coffee = map(find_coffee, menu)
print(map_coffee)

for x in map_coffee:
    print(x)

filter_coffee = filter(find_coffee, menu)
print(filter_coffee)

for x in filter_coffee:
    print(x)




# LIST comprehension
data = [2,3,5,7,11,13,17,19,23,29,31]

# Ex1: updating the same list
data = [x+3 for x in data]
print("Updating the list: ", data)

# regular foor loop for the above expression
for x in range(len(data)):
    data[x] = data[x] + 3

# Ex2: creating a different list with updated value
new_data = [x*2 for x in data]
print("Creating a new list: ", new_data)

# Ex3: if condition, multiples of 4
fourx = [x for x in new_data if x%4 == 0]
print("Divisible by 4: ", fourx)

# Ex4: update the list with if condition
fourxsub = [x-1 for x in new_data if x%4 == 0]
print("Divisible by 4 minus 1: ", fourxsub)

# Ex5: range function:
nines = [x for x in range(100) if x%9 == 0]
print("Nines:", nines)




# DICTIONARY comprehension
using_range = {x:x*2 for x in range(12)}
print("Using range() function: ", using_range)


# Lists 
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using 1 input list
numdict = {x:x**2 for x in number}
print("Using one input list to crerate dictionary: ", numdict)

# Using 2 input list
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using 2 input lists to create a dictionary: ", months_dict)

# new_dict ={key:value for (key, value) in zip(list1, list2)}



# SET comprehension:
set_a = {x for x in range(10, 20) if x not in [12, 14, 16]}
print(set_a)



# GENERATOR comprehension:
data = [2,3,5,7,11,13,17,19,23,29,31]

gen_obj = (x for x in data)
print(gen_obj)

print(type(gen_obj))

for items in gen_obj:
    print(items, end = " ")


a = [[96], [69]]
print(''.join(list(map(str, a))))
print(type(a))

z = ["alpha","bravo","charlie"]
new_z = [i[0]*2 for i in z]
print(new_z)

def summation(n):
   if n == 1:
       return 0
   return n + summation(n-1)

a = summation(5)
print(a)