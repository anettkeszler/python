# FUNCTIONS

# define a function
def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100, 2)

# call a function
print("Total tax is: ", calculate_tax(175.00, 15))
print("Total tax is: ", calculate_tax(175.5678, 22))


# Get min and max
def get_min_max(numbers):
    return min( numbers), max(numbers)

numbers = [5, 9, 34, 900, 567, 23, 1, 56, 103455]
minimum, maximum = get_min_max(numbers)
print(f"Minimum number is {minimum}, maximum number is {maximum}")


# VARIABLE SCOPES
global_variable = 10

def func_1():
    enclosed_variable = 8
    def func_2():
    
        local_variable = 5
        print(f"Access to global variable: {global_variable}")
        print(f"Access to eclosed variable: {enclosed_variable}")

    func_2()

print(func_1())
