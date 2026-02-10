# MODULES

# return all the possible location that the interpreter look for when searching for modules, 
# including the current working directory --> /Users/anettkeszler/GitHub/Python
import sys

locations = sys.path

for location in locations:
    print(location)


# adding a new path to look for modules 
# the sys.path list now has a new directory where it will look for modules
sys.path.insert(1, r'/Users/anettkeszler/GitHub/Python/assignments')

# now I have access to the sample_module
import sample_module
print(sample_module.name)


# use calendar module
import calendar 

# return the number of leap days between the 2 given years
leapdays = calendar.leapdays(2000, 2050)
print(leapdays)

# boolean
is_leap = calendar.isleap(2000)
print(is_leap)  # True

# Writing import statement
import math

root = math.sqrt(9)
print(root)         # 3.0


# dir() returns all function names in a module
print(dir(math))


# reload() function
# we are going to reload the sample_module 
import importlib

print("1st reload")
importlib.reload(sample_module)

print("2nd reload")
importlib.reload(sample_module)

print("3rd reload")
importlib.reload(sample_module)