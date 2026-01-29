# USER INPUT 
# input() and print() functions

email = input("Please enter your email address: ")
print(email)

# User input is always a string, you need to convert it to integer to calculate with it
num1 = int(input("Please add the first number: "))
num2 = int(input("Please add the second number: "))
result = num1 + num2

print(" Adding the value of {} and {} = {}".format(num1, num2, result)) # Direct formatting


# Concatenation
str1 = input('Please enter your first name: ')
str2 = input('Please enter your second name: ')
print('Hello, ' + str1 + ' ' + str2)
# formatting
# print("Hello, {} {}".format(str1, str2))

num_1 = input('First number is: ')
num_2 = input('Second number is: ')
user_sum = float(num_1) + float(num_2)
print("The sum of: " + num_1 + " and " + num_2 + " is " + str(user_sum))    # String concatenation 


# DIRECT FORMATTING
# you can control the order by specifying the numbers inside the curly brackets 

print("I like {0} more than {1}.".format("oranges", "grapes"))
# I like oranges more than grapes.

print("I like {1} more than {0}.".format("oranges", "grapes"))
# I like grapes more than oranges.

