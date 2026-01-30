# DICTIONARY
# access the value based on the key
my_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
print(my_dict[1]) # Coffee

# update the dictionary by replacing an item to another
my_dict[2] = 'Mint Tea' # update the value based on the key
print(my_dict)      # {1: 'Coffee', 2: 'Mint Tea', 3: 'Juice'}

del my_dict[3]
print(my_dict)  # {1: 'Coffee', 2: 'Mint Tea'} , delete the key-value pair based on the key

# adding a key-value pair to the dictionary
my_dict[3] = 'Cocoa'
print(my_dict)       # {1: 'Coffee', 2: 'Mint Tea', 3: 'Cocoa'}   


# Iterate over dictionaries

# this case only prints the keys:  1, 2, 3
for x in my_dict:
    print(x)        
    

for key, value in my_dict.items():
    print(str(key) + " : " + str(value))

# Output: 
# 1 : Coffee
# 2 : Mint Tea
# 3 : Cocoa