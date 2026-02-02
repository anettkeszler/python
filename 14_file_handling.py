# FILE HANDLING

# open and read from a file, than close the file
file = open('/Users/anettkeszler/GitHub/Python/file handling/test.txt', 'r')
data = file.readline()  
print(data)
file.close()


# with open --> closes the file automatically
with open('/Users/anettkeszler/GitHub/Python/file handling/test.txt', 'r') as file:
    data = file.readline()
    print(data)


# creating a new file: file.write("")
with open('/Users/anettkeszler/GitHub/Python/file handling/new_file.txt', 'w') as file:
    file.write('This is a new file created!') 


# Editing a file with multiple lines:
# file.writelines("") --> accepts a list 
try: 
    with open('/Users/anettkeszler/GitHub/Python/file handling/new_file.txt', 'a') as file:
        file.writelines(['\nThis is the first line!', '\nThis is the second line!', '\nThird line'])
except FileNotFoundError as e:
    print(e, "File not exists.")


# Reading files: 
# read() - provides the whole content of the file in a string
with open('/Users/anettkeszler/GitHub/Python/file handling/new_file.txt', 'r') as file:
    data = file.read()
    print(data)
    print(type(data))

# readline() - returns a single line as a string

# readlines - reads the whole content of the file and returns it as an ordered list allowing iteration on it