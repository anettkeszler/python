# EXCEPTION HANDLING
def divided_by(a, b):
    return a / b

print(divided_by(40, 4))
# print(divided_by(10, 0)) # ZeroDivisionError: division by zero

# to handle this, use try-except block:
try:
    result = divided_by(40, 0)
except Exception as e:
    print("Something went wrong.", e)   # Something went wrong. division by zero
    print(e.__class__)                  # <class 'ZeroDivisionError'>


# you can add more specific exceptions:
try:
    result = divided_by(40, 0)
except ZeroDivisionError as e:
    print(e.__class__)
    print("You can not divide by zero,", e)
except Exception as e:
    print("Something went wrong, ", e)
    print(e.__class__)

# EXERCISE

# IndexError
# Starter code
items = [1,2,3,4,5]

# item = items[6]
# print(item)     # IndexError: list index out of range

try:
    item = items[6]
    print(item)
except IndexError as e:
    print(e.__class__)
    print("IndexError,", e)


# ZeroDivisionError: 
def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("ZeroDivisionError,", e)
    except Exception as e:
        print("Something went wrong,", e)

result = divide_by(29, 0)
print(result)

# FileNotFoundError
try:
    with open('file_not_exist.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e.__class__)
    print("FileNotFoundError,", e)