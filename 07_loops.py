# FOR LOOP
str = "Looping"

for char in str:
    print(char)


for i in range(10):
    print(i)


favorites = ["Banana", "Tiramisu", "Creme Brulee", "Chocolate cake"]

for item in favorites:
    print("I like this dessert:" , item)

# WHILE LOOP
count = 0
while count < len(favorites):
    print("I like this dessert", favorites[count])
    count += 1 
# if I dont increase the count, it will end up with an infinite loop --> 
# it will keep looping until the compiler stops it from running out of memory


# enumerate() - to access the index in a for loop
for idx, item in enumerate(favorites):
    print(idx, item)


# CONTROL FLOWS - break, continue, pass

# 'break' will exit the loop when the given condition is met
for dessert in favorites:
    if dessert == "Apple":
        print(f"This is my favorite dessert: {dessert}")
        break       
else:
    print("Not a dessert on my list.")
    
# 'continue' allows you to skip over a section of the loop but then continue on with the rest
for dessert in favorites:
    if dessert == "Tiramisu":
        continue
    print(f"Other dessert I like: {dessert}")

# 'pass' - placeholder, it does nothing and allows the program to continue execution normally
for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert) 


for i in range(10):
    if i == 3:
        continue # Skip this iteration
    if i == 7:
        break # Exit loop
    print(i)

# NESTED FOR LOOP
# outer loop
for i in range(10):
    # inner loop
    for j in range(10):
        print(0, end = " ")
    print()