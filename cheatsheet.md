# Cheat Sheet for Python 

- **Programming** is a set of instructions in a language that the computer understands, to perform a specific task. 

### Python
- was released in 1991 by Guido van Rossum
- one of the most popular programming languages to learn 
- has lots of frameworks and libraries
- widely used in all areas of business (web developement, AI, machine learning, data analytics, applications)
- easy to learn and get started with
- require less code in comparison to Java, so it makes developers very productive and allows projects to be completed more quickly 
- "write less, do more" philosophy

### Installing Python path (Mac)
- **Xcode**: command-line tool, an integrated development environment (IDE), and you need to be installed to use brew
- **homebrew**: free, open-source **package manager** for macOS and Linux that simplifies installing, updating, and managing software via the command line.
```
python --version
brew install python 
python3 --version
```
- homebrew will install python 3.x. version
- after installation, you need to set the paths to point to the brew install of python3
- First, let's figure out where it was installed by the package manager brew. Run the following command: 
```
brew info python
```
- ```/opt/homebrew/opt/python@3.x/libexec/bin``` is the one you want to use and set for your path.

1. Open zsh or bash (depending which shell you are using)
- Zsh: ```vim ~/.zshrc```
- Bash: ```vim ~/.bashrc```

2. Add the following line and remember to replace 3.x with the Python version that was installed on your system: 
```export PATH="/opt/homebrew/opt/python@3.x/libexec/bin:$PATH" ```
3. esc + wq!
4. Run the following:
- For Zsh shell: ```source ~/.zshrc``` 
- For Bash shell: ```source ~/.bashrc``` 

### Running Python code - Python Shell or VSCode
- in VSCode set up the python interpreter: search for 'python: select interpreter' (cmd+shift+p), choose the one it's recommended or which comes with the most recent version 
- **Python interpreter** is the program that reads and executes Python code. It converts Python code into machine code that computer can execute. 

Different ways to run Python code:
1. **Interactive Shell in Terminal**:<br>
- to start: ```python```
- to exit: ```exit()```
- useful for running and testing small scripts
- no need to create a .py file

2. **Run a Python file**: <br>
```python3 hello.py```
- It is better to run Python in VSC compared to running it in the Python shell or in the command line, because VS Code features include auto-completion, code syntax, highlighting and debugging, whitespace and indentation helpers. 

3. **Run a Python file in Interactive mode**:<br>
```python3 -i hello.py```

### Comments in Python code
- There are multiple reasons why you need to add comments to a code file: <br>
    - Explaining what the code is intended to do<br>
    - Let developers know that code is deprecated<br>
    - Add TODO comments for work to be completed at a later time<br>
- Single-line comments: ```# I'm a single line comment```
- Multi-line comments: triple single or double quotes (``` OR """) - used for docstrings or long comments
- Inline comments: ```x = 2  # resetting size```

### Variables
- To create a variable you need to declare a name and assign it a value  
- To change the value of a variable that has already been declared, you only need to reassign or redeclare it 
- **Naming conventions**:
    - **camelCase**: first letter is lowercase, and the first letter of every world after is uppercase with no space between words (myFirstName) 
    - **snake_case**: everything is lowercase, but use an underscore between words (my_first_name)
- When creating a variable, python automatically assigns the datatype for you
```
name = "Leo"    # String
age = 7         # Integer
height = 5.6    # Float
is_cat = True   # Boolean
flaws = None    # None type
```
- You can declare multiple variables and assignt them to the same value (parallel assignment): 
``` 
a = b = c = 10
```
- You can declare multiple variables and assign them to multiple values (chained assignment):
```
a, b, c = 1, 2, 3
```
- You can delete a variable:
```
del x
```
### Data Types
- to determine a type of a variable, use type() function, which provides the class type 
- when you declare a variable in Python, the datatype is automatically assigned based on the value
- Use ```None``` to represent missing or optional values 
- **Numeric**: 
    - **Integer**: 
        - integer class (```<class 'int'>```) represents any whole number with no decimal points (positive or negative)
    - **Float**: 
        - contains decimal point (2.9)
        - represented by the float class (```<class 'float'>```) 
    - **Complex Number**: 
        - represents the complex class (```<class 'complex'>```)
        - contains both real and imaginary numbers (a = 10 + 10j)
- **Sequence**: 
    - **String**: 
        - sequence of characters that is enclosed in a single or double quotes
        - represented by the string class (```<class 'str'>```)
    - **List**: 
        - sequence of one or more similar or different types of data
        - example_list = [10, 'hello', 24.2] -->  ```<class 'list'>```
        - each items can be accessed by its index
        - mutable: items can be changed
    - **Tuples**: 
        - contain an ordered sequence of one or more types
        - but they are immutable: the values cannot be modified or changed 
        - represented by the tuple class (```<class 'tuple'>```)
        - example_tuple = (10, 'hello', 24.2)
- **Dictionary**: 
    - stores data in a key-value objects
    - each value can be accessed directly by its key
    - can store any data type
    - ed = {'a': 23, 'b':44.3}
    - ed['a'] --> 23
    - ```<class 'dict'>```
- **Boolean**: 
    - true or false
    - type(False) / type(True) --> ```<class 'bool'>```
- **Set**: 
    - unordered and non-indexed collection of non-repeated values 
    - example_set = {1, 'hello', 4.5, "A"}
    - type(example_set) --> ```<class 'set'>```
- **isinstance()**: check for a scpecific type 
```
isinstance(3.14, float)     # True
```
- **issubclass()**: checks if a class is a subclass
```
issubclass(int, object)     # True
```

### Type Casting - data type conversion / + 02_type_casting.py
- typecasting is the process of converting one data type to another 
- **implicit data type conversion**: 
    - is automatical by Python's compiler to prevent data loss (int --> float). 
    - it only works if the data types are compatible (int - float). 
- **explicit data type conversion**: when implicit conversion throws a type error (TypeError)
    - int('55') --> 55
    - str(45) --> '45', it converts **any data type** into a string datatype
    - float('20.45') --> 20.45
    - bool()
    - tuple()
    - list()
    - set()
    - dict() 
    - ord() --> returns an integer representing the underlying unicode character 
    - hex() --> converts a given integer to a hexadecimal string 
    - oct() --> takes an integer and returns a string representing an oct to a number  

### User input, console output (input(), print()) / + 03_input_output.py
- input() function is designed to get data from the user
```
email = input('Please enter your email address: ')
print(email)
```
- print() function is used to outputs in Python
```
print(1, 2, 3)              # comma separated arguments
print(1 + 3)                # aritmetic 
name = 'John'
print('Hello ' + name)      #string concatenation

a = 10
b = 5
result = a + b
print('Adding the value of {} and {} = {}'.format(a, b, result))    # direct formatting 
```
### Strings / + 04_strings.py
- String is a sequence of characters enclosed in quotes (single or double) 
- if your string is too long for one line, you can add a backslash (```\```) at the end of each line to create a multi line declaration
- each character in the sequence can be accessed based on its index 
- length of the string: len() function
- concatenation: joining of separate strings with '+' operator 
- use ```'\n'``` to create a line break in a string
- to write a backslash in a normal string, write '```\\```'
- **String operations**: 
    - concatenation with the aritmetic operator (+)
    - multiply with * operator
- **String methods**: upper(), lower(), strip(), replace(), split(), join() 
- **String indexing and slicing**: 
    ```
    string[start:stop:step]
    ```
- **String formatting**: 
    - using f-string
    - format() method 

### Math and Logical operators / + 05_mathematical_operators.py
Operations in Python can be:
1. **Mathematical / Arithmetic Operators**: 
    - addition: +
    - subtraction: -
    - division: / 
    - multiplication: * 
2. **Logical Operators**: <br>
They used in **conditional statements** to determine a True or False outcome
    - and: checks for all conditions to be true 
    - or: checks for at least one conditions to be true 
    - not: return false if the result is true 
3. **Comparison Operators**:
```
x == y      # equal to
x!= y       # not equal to
x < y       # less than
x =< y      # less than or equal to
x > y       # greater than
x => y      # greater than or equal to
```

### Conditional statements / + 06_conditionals.py
- Control flow refers to the order in which the instructions in a program are executed 
- **Control flows can be**:
    - **Conditional** (statements): if, else, else if (elif)
    - **Loops**: for loop, while loop 

#### Match statement 
- compares a value to several different conditions until one of these conditions is met 
- use match statement when you **test a variable against many conditions** 
- match statement is an alternative of the if statement 

### Loops / + 07_loops.py
- Looping is used to iterate through the sequence and access each item inside the sequence

- FOR LOOP:
    - The for loop is based on the size or length of the elements to iterate over. 
    - in a standard for loop, I don't have access to the index, but I can use the enumerate() function to do that:
    ```
    favorites = ['Banana', 'Apple', 'Tiramisu', 'Cake']

    for idx, item in enumerate(favorites):
        print(idx, item)
    ```
- WHILE LOOP:
    - based upon a condition being true. Once the condition is no longer true the loop stops. 
    - need the set up a condition, than a counter and set the count to 0
    - the loop will run while the count is less than the length of the list 
    - I have to increment the count by 1 at the end of the block, if not, it will end up in an infinite loop (keep looping until the compiler stops it from running out of memory)

#### Control flows:
- So far you looped over sequences based on the length of the data you wanted to iterate over 
- But in many cases, not necessary to iterate over the whole sequence, and you can control the flow of the loop and exit when a specific condition is met
- Control statements: **break, continue, pass**
    - break: will exit the loop when the given condition is met
    - continue: allows you to skip over a section of the loop but then continue on with the rest
    - pass: acts as a placeholder, allowing you to include an empty block of code without causing a syntax error. It does nothing and allows the program to continue execution normally.

### Functions / + 08_functions_variable_scope.py
- function is a piece of code that can be re-used repeatedly
- input --> function body --> output

#### Useful built-in functions
```
callable()      # Checks if an object can be called as a function
dir()           # Lists attributes and methods
globals()       # Get a dictionary of the current global symbol table  
hash()          # Get the hash value
id()            # Get the unique identifier
locals()        # Get a dictionary of the current local symbol table
repr()          # Get a string representation for debugging

```
### Variable scoping
- The purpose of scope is to protect the variable 
- Scopes in Python: **local, enclosed, global, built-in (LEGB)**
- Variables in Python are implicitly declared when you define them, meaning unlike other programming languages, there is no special declaration for them
- Scope determines where your variable is visible and directly accessible in your program 

1. **Local Scope**: 
- refers to a variable that is declared inside a function
- outside of the function will not have access to it
- when you attempt to access the variable outside of the function, Python raises a **NameError** because the variable is out of scope.
- (NameError: name 'total' is not defined)

2. **Enclosing Scope**: 
- refers to a function inside another function or what is commonly called a nested function

3. **Global Scope**: 
- accessible from anywhere in the code 
- when a variable is declared outside of a function

4. **Built-in Scope**: 
- accessible from anywhere in the code
- built-in functions and objects, such as print()and def 
- Built-in scope covers all the language of Python

### Data Structures
- A Collection is any data structure that can store multiple items 
- If an Object is a Collection, you can loop through it. (String is also iterable.)
- Use len() to get the size of a collection 
- Built-In Data Structures in Python: 
    - List
    - Tuple
    - Set
    - Dictionary
- User-Defined Data Structures in Python:
    - Stack
    - Queue
    - Tree
    - LinkedList
    - Graph
    - HashMap

### Lists / + 09_lists.py
- Lists are a sequence of one or more different or similar datatypes 
- In Python, it is a dynamic array that can hold any datatype 
- List items can be accessed by its index
- List is iterable, you can iterate over it with a foor loop to access all items
- List methods:
```
nums.append(4)                  # add 4 at the end
nums.insert(0, 5)               # insert 5 at index 0
nums.extend(["z", 3, True])     # extend with iterable 
nums.remove(7)                  # remove first 7 
nums.pop(0)                     # will remove the first item
del nums[index]                 # removes the item on given index                   
```
### Tuples / + 10_tuples.py
- my_tuple = ()
- tuples can accept any data types
- tuple.count("hello") - counts the occurance of the given value
- tuple.index("hello") - gets the index of a given value
- you can iterate over a tuple with a for loop
- key difference between lists and tuples, that tuples are **immutable**, means that they **can not be changed**
- **Immutability**: Once a tuple is created, its elements cannot be changed. 
- While you can access elements using indexing, you can't modify them or add new ones after creation

### Sets / + 11_sets.py
- Sets are collections with **no duplicates** and **unordered item** 
- Set is **not a sequence**, so it **cannot be indexed**. You cannot reach the items by its index (not ordered)
- Set methods:
    - **set.add(value)** - item will be added at the end
    - s**et.remove(value)** - given value will be removed
    - **set.discard(value)** - same as remove
- **Mathematical operations on sets**:
    - **Union**: merges the 2 sets, but exclude the duplicates
    ```
    set1.union(set2) 
    set1 | set2
    ```
    - **Intersection**: get back the values which occures in both sets (& - ampersand)
    ```
    set1.intersection(set2)
    set1 & set2
    ```
    - **Difference**: get back all the elements that are only in set1, and not in set2
    ```
    set1.difference(set2)
    set1 - set2
    ```
    - **Symmetrical difference**: get back all the elements that are present in set_a or set_b, but not in both sets (carrot(^) operator)
    ```
    set1.symmetric_difference(set2)
    set1 ^ set2
    ```

### Dictionaries / + 12_dictionaries.py
- Dictionaries access values based on keys (not on index as lists)
- Faster and more flexible as lists: you can go straight to the item you need based on its key
- we assign the key to a specific value --> called **key-value pair**
- Mutable, values can be changed or updated 
- Access the value based on the key:
```
print(my_dict[2])   # 'Tea' - gives you the value corresponding to the given key
```
- Update dictionary by replacing an item:
```
my_dict[2] = "Mint tea"   # updates the value based on the key
```
- Delete a key-value pair from the dictionary based on the key:
```
del my_dict[3]
print(my_dict)  # {1: 'Coffee', 2: 'Mint Tea'} 
```
- Adding a key-value pair to the dictionary:
```
my_dict[3] = 'Cocoa'
print(my_dict)          # {1: 'Coffee', 2: 'Mint Tea', 3: 'Cocoa'}
```
- If I try to add a duplicate key, it doesn't allow this, keys must be unique

### Args and kwargs(keyword arguments)
- benefits: you can pass any amounts of **non-keyword variables and keyword arguments**
- **ARGS: non-keyword variables**
- Instead of passing 3 arguments, using *args will alow to pass any arguments by calling the function 
```
def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(4, 5, 6)) # 15
```
- **KWARGS: keyword arguments**
- let's calculate the total bill in a restaurant
```
sum_of(**kwargs):
    sum = 0
    for key, value in kwargs.items():
        sum += value
    return round(sum, 2)

print(sum_of(coffee=2.99, cake=4.55, juice=2.89))
```

### Exceptions, Errors, Exception handling / + 13_exception_handling.py
1. **Syntax Error**: 
    - usually caused by the developer (misspelling/typo or indentation issues)
    - has minimal impact, because most IDEs warns the developer and gives ideas how to fix them 
2. **Exception Error**: 
    - an error during execution/runtime causes an exception  
    - exceptions need to be handled by the developer
    - Common exceptions:
        - ValueError: invalid value
        - TypeError: wrong type
        - IndexError: list index out of range
        - KeyError: dictionary key not found
        - FileNotFoundError: file doesn't exist

### File handling functions: open() and close() / + 14_file_handling.py
- Open:
    - ```open()``` function is used for reading, writing and creating files 
    - open() function accepts 2 arguments --> open(<file_name> OR <file_location>, <mode>)
        - mode indicates the action --> reading, writing, creating
            - 'r' --> open and read in text format
            - 'rb' --> open and read in binary format
            - 'r+' --> open, read and write 
            - 'w' --> open for writing 
            - 'a' --> open for editing or appending 
    - ```close()``` function: no arguments, it closes the open connection 
    - ```with open()``` function: it closes the file automatically, and better with exception handling

### Programming Paradigms in Python 
- The main purpose of a programming model is to structure your code
- In Python, we use 3 ways to structure our code:
    - **Procedural**
    - **Functional**
    - **Object Oriented**
- DRY - Don't Repeat Yourself  
- You will likely use a combined approach that relies on procedural, object oriented and functional programming paradigms 

### Procedural paradigms / 15_procedural_programming.py
- writing step-by-step instructions that program executes
- is an imperative programming paradim based on the concept of modularity, where programs are organized into sequence of instructions, routines or subroutines (functions) to achieve a goal
- it emphasizes a top-down, step-by-step approach, making ideal for smaller projects and often for learning programming fundamentals
- key aspects:
    - Procedures/Functions: the code is broken down into reusable, self-contained block of code
    - Linear control flow: program follows a sequential, top-down structure, executing instruction in a specific order
    - Data and Procedures Separation: data and procedures are treated as distinct entities, with data often stored in global or local variables.
    - Modularization: Complex problems are broken down into smaller, manageable, and independent procedures, which helps with code organization and maintenance.
    - Control Structures: It utilizes loops, conditionals, and sequence to manage the execution flow.
- Pros: easy to understand, learn and debug, efficient for small to medium tasks, code reusability
- Cons: becomes difficult to manage for large and complex system, poor data security due to reliance on global data
 
 #### Algoritms
 - an algoritm is a series of steps to solve a problem 
 - refactoring an algoritm is a standard part of the software development cyclem, to making it faster or to perform better
 - code is measured by:
    - time (how long it takes to run the code)
    - space(how much memory it uses)
 - an algorithm efficiency is measured by BigO Notation in terms of time and space 
 - **Big O notation** is a fundamental concept in computer science and programming that helps you analyze and describe the efficiency of algorithms. It provides a standardized way of expressing how the runtime or resource usage of an algorithm grows as the size of the input data increases.
    - **Constant time - O(1)** :  
        - same time and space regardless of the size
        - the runtime does not depend on the size of the input data
        - it remains constant, making it the **most efficient scenario**.
        - Example:
            - **dictionary**: to get the value of an item you need to have the key
            - the key is a direct pointer to the value and does not require any iteration to find 
            - Accessing an element in an array by its index
    - **Linear time - O(n)**: 
        - this will grow depending on the size of the input 
        - array of integers with a range of 100, it will very fast. But if it increased to 1 million, it take a lot longer to complete 
        - Example: 
             - Searching for a specific value in an unsorted list
    - **Logaritmic time - O(log n)**: 
        - the runtime grow logarithmically with the size of the input data
        - Logarithmic time complexity is considered very efficient
        - binary search: it splitting the list into 2 parts , and each time to check if a target is less than or greater than one. 
    - **Quadratic time - O (n^2)**: 
        -  the runtime grow with the square of the input size
        - Example: 
            - nested list
            - Bubble Sort
    - **Exponencial time - O(2^n)**:
        - this occurs in algorithms where for each increase in the size of the data set, the runtime is doubled. 
        - fibonacci 
    - **Factorial runtime - O(n!)**:
        - terrible runtime 
        - Any algorithm that performs permutation on a given data set is an example of O(n!)
#### **A Quick Breakdown**:
- Fastest: **Constant time** - **O(1)** Lightning-fast! - accessing a value based on its key in a dictionary , or in an array by its index
- Pretty Fast: **O(log n**) - **Logarithmic Time**: Still quite speedy! It grows slowly as you add more data. - binary search 
- Moderate: **O(n)** - **Linear Time:** Respectable speed! If you have twice as much data, it takes about twice as long. It's like looking through a list of names one by one to find a match.
- Slower: **O(n log n)** - **Linearithmic Time**: It's faster than quadratic but slower than linear. An example of O(n log n) time complexity is the Merge Sort algorithm, which divides an array into smaller parts, sorts them, and then merges them back together.
- Slower Still: **O(n^2)** - **Quadratic Time**: Getting slower as you add data. Like checking every combination of items on a list against each other – not great for large lists, like Bubble sort
- Quite Slow: **O(2^n)** - **Exponential Time**: Now we're talking about slow! It grows rapidly as you add data. Imagine a puzzle where you have to try every possible combination – it's really slow even for small puzzles.
- Incredibly Slow: **O(n!)** - **Factorial Time**: The slowest of all! It's like solving a complex puzzle where the number of possible arrangements explodes as you add more pieces. Practically unusable for large problems. An example of O(n!) time complexity is generating all possible arrangements (permutations) of a list of items, like finding all possible seating arrangements for a group of people.

### Functional Programming



### Modules / + 18_import_modules.py
- They are building blocks for adding functionalities to your code, so you don't need to continually redo everything 
- any file with .py extension can be a module
- Advantages of using modules:
    - **Scoping** means that modules create a separate namespace: 2 different modules can have functions with the same name 
    - **Reusability**: most important advantage
    - **Simplicity**: each module is built with a simple purpose in mind, and helps avoiding interdependency among these modules 
- Modules are defined by their usage > Regular expression module managing regular expressions 
- Types of Modules: different in these modules is the way they are accessed 
    1. **Built-in modules**: part of the standard Python library 
            import math: the interpreter first tries to find a built-in modules 
            Since code execution in Python is serial, you must import the module first before you execute any function inside of it 
    2. **User-defined modules** 

#### Accessing modules:
- any python file can be a module (import sample --> will import the sample.py file)
- the modules are searched by the interpreter in the following sequence: 
    1. current directory path 
    2. built-in module directory 
    3. PYTHONPATH (and environment variable with a list of directories)
    4. Installation dependent default directory 

- command+click on the module to explore all the functionalities

#### Writing Import statements
- importing the whole math module
```
import math 
math.sqrt(9)
```
- instead of loading the entire module, import only the sqrt function
```
from math import sqrt
sqrt(9)
```
- Use alias for the module name
```
import math as m
m.cos(0)
```
```
from math import sqrt as s
s(9)
```
- import a list of functions from a module:
```
from math import sqrt, factorial, cosine
```
- import all functions from a module: (not recommended)
```
from match import * 
```

-dir() function: returns all functions in a module
```
print(dir(math))
```
#### reload() function
- reloads an imported module in Python 
- reload() function is in the importlib module (import importlib)

### Modules, packages, libraries
- **Modules**: a module is a single .py file containing Python code. When you import a module, you bring its definitions and statements into your current script’s namespace.
- **Packages**: is a collection of related modules organized in a directory hierarchy. The presence of an __init__.py file within a directory signals to Python that it’s a package. This allows for a more structured way to manage multiple modules that work together.
- **Library**: it refers to a collection of packages. This is the broadest term, referring to a collection of pre-written code used to perform specific tasks. A library can be composed of single modules, multiple packages, or a mix of both. The Python Standard Library is a prime example, offering a vast array of functionalities. Essentially, all packages are a type of library, but not all libraries are necessarily structured as multi-module packages.

- To install packages that are not a part of the standard library, use pip (package installer for Python). 
- To check the status of pip installation:
```
python -m ensurepip --upgrade
```
- To install packages:
```
python3 -m pip install "SomePackage"
python3 -m pip install requests
```
- The packages that you can install often have a number of classes, functions, sub-packages and members. 

- sub-packages: 
to import a sub-package:
```
import matplotlib.pyplot
```

### Packages
- Packages are bundled collection of modules serving a specific purpose
- a package is a directory or folder (vs module, which is a file)
```
from <package> import <module>
```
- 'module' holds the function we want to use
- pip: package manager
- PyPI: Python Package Index, where you can find unpublished packages
- Package categories:
    - **Built-in packages**: no need to install (os, sys, csv, json, importlib, re, math, intertools)
    - **Data Science**: for data manipulation: numPy, sciPy, Pandas; for data visualization and image processing: open cv, matplotlib
    - **Mechine Learning and AI**: PyTorch, Tensorflow, Keras, SciPy, Scikit-learn 
    - **Web and GUI Development**: Flask (lightweight micro-framework), Django (full stack framework), cherry pie, pyramid, selenium, beautiful soup
#### Data analysis packages
- Most popular packages:
    - **Scikit-learn**
    - **Pandas**: Python Data Analysis 
        - cleaning, analyzing and manipulating data
        - primary data structure used in pandas are Series(single dimensional) and DataFrames(multi-dimensional)
        - pandas most common applications are reading csv files and json objects 
        - ```import pandas as pd```
    - **NumPy**: Numerical Python, 
        - powerful library forming the base for libraries such as Scikit-learn, Scipy, Metplotlib
        - commonly used data structure is nd-array (n-dimensional array)
        - ```import numpy as np```
    - **Matplotlib**: visualization library 
        - static, interactive and animated visualizations
        - ```import matplotlib.pyplot as plt```
#### Machine Learning and AI packages:
- machine learning is a subsection of AI and deals with algorithms for training and generating insights from data 
- some fields in ML:
    - natural language processing 
    - deep learning 
    - sentiment analysis
    - recommender engines 
    - speech recognition  
#### Big Data Analysis
- Data Source --> Data Storage --> Filter & Transform Data --> Analysis and Stroage --> Report and Visualization
- Libraries that are specific to Big Data analysis:
    - RedShift
    - BigQuery
    - PySpark
    - Kafka
    - Pydoop
### Libraries
- Libraries are collection of packages with specific purpose 
#### Web frameworks
- software applications designed to provide a standard way to build, deploy and support web applications 
- helps developer to focus on application logic by automating redundand tasks 
- reliable, stable and easily maintainable, saving time and effort 
- helps to handle tasks, such as form processing, routing request, connection with databases, user authentication. 
- they provide debugging and testing tools 
- 3 types of web frameworks in Python: 
    - fullstack(Django, Pyramid): includes form generations and validations, template layouts, HTTP rrequest handling, webserver connections, database connection handling 
    - microframeworks(Flask, Bottle, Dash, CherryPy): used in smaller web projects and building APIs
    - asynchronus: handles a large sets of concurrent connections 

### Testing
- Testing is a process of evaluating and verifying the various software applications and products in terms of performance ,correctness and completeness 
- It helps identify bugs , gaps in a product, defects, missing requirements 
- Nowdays testing are integrated at the early stages of development (TDD)
#### Types of Testing
1. Unit/Component testing: the program tests specific individual components by isolating them. You usually write these tests while writing the code 
2. Integration Testing: combines the unit test, and test the flow of data from one component to another. You test if the data is correctly fetched from a database within the python code, and if you have sent it to the web page  
3. System Testing: tests all the software 
4. Acceptance Testing: ready for deployment, it's expected to be bug free and meet the set standards 

- White box texting: tester has knowledge of the code design and functionalities 
- Black box testing: the tester has no idea about the internal implementation

- keywords: testing early and testing frequently

#### Test automation packages / + 19_addition.py, 19_test_addition.py
- units, regresssion, integration tests: they can be automated 
- Ideal steps are: 1. preparing test environment --> 2. run the test script --> 3. analyzing the result 
- Unittest/PyUnit: built-in testing package, it supports test automation, independent testing modules, aggregation of tests into collections 
- **Pytest**: native python library, most popular testing framework for automation
- Robot: Keyword-driven development capabilities, used for acceptance testing, robotic process automation, and TDD 
- Selenium: primariliy used for web application testing 
- in our test file: (test_addition.py) 
```
import addition (name of the file we want to test)
import pytest
```
- to run the test file:
```
python3 -m pytest test_addition.py
python3 -m pytest test_addition.py::test_add
```
- some other flag options:
```
-v for verbose
-q quiet mode
-s allows the print statement inside the functions to be executed
-x is to flag the tests to stop execution after first failure
-m is used to mark a specific function
-k is a flag for searching and running tests with a specific keyword
--tb is to disable the traceback code of errors
--maxfail n specifies maximum number of test fails allowed
```
### Test Driven Development (TDD)
- in TDD write the tests first and than the code, so that tests will pass 
- TDD follows an iterative approach beginning with writing the test cases 
- Red-green refactor cycle:
    - step1: write the test for a feature that fails 
    - step2: write code in accordance with the test
    - step3: run the tests expecting them to fail 
    - step4: evaluate the error and refactor the code as needed 
    - step5: rerun the process 
#### TDD vs traditional testing / 20_findstring.py, 20_test_findstring.py
- TDD: 
    - requirements and standards are highlighted from the beginning 
    - working in cycles over the code gives the competence to easy to refactor 
    - smaller code with early bug fixes 
    - code extensibility 
- Traditional testing: 
    - code then test

### Functional Programming / + 16_functional_programming.py
- Pure function does not change or have any effect on a variable, data, list etc beyond its own scope 
- Pure functions: cannot access and modify variables on the global state, only in the local state 
- Traditional functions: can access and modify both global and local variables 
- Pure functions: output does depend on the input 
- Traditional functions: the output doesn't depend on inputs
- Functional programming is a programming paradigm that utilizes functions for clean, consistent and maintainable code 
- It doesn't change the data outside the scope of the function 
- the language allows function to be passed as an argument and return a function to its caller 
 - A pure function will keep your code cleaner, easier to debug and easier to extend 
#### Recursion
- is a function that calls itself 
- it creates a pattern of repeating itself over and over 
- always consider the result, otherwise it will end in an infinite loop 
- reverse a string with recursion:
```
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]
    
print(string_reverse("reversal"))
```
#### Map and filter
- to process a list and generate a new list 
- map() function: takes the function as an argument and passes the menu list values into the function one-by-one 
- difference between map and filter: 
    - map() takes all objects in the list and allows you apply a function to it 
    - filter() do the same, but take the results and creates a new list with only the true values 

### Comprehension
- Comprehensions are a way to create a new sequence from an already existing sequence
1. **List Comprehension**:
- Comprehensions provide a short-hand and elegant way of updating sequences.
```
[ <expression> for x in <sequence> if <condition>] 
```
2. **Dictionary Comprehension**:
- Dictionary comprehension takes one or two lists as input and creates a dictionary out of it.
```
dict = { key:value for key, value in <sequence> if <condition> } 
new_dict ={key:value for (key, value) in zip(list1, list2)}
```
- When the two lists are of unequal length, the length of the shorter list is the length of the dictionary.
3. **Set Comprehension**:
- The set comprehension deals with the set data type and it's very similar to list comprehension. 
- The only key difference is the use of curly brackets for sets instead of square brackets as in lists.
- 'not in' keyword
```
set_a = {x for x in range(10, 20) if x not in [12, 14, 16]}
```
4. **Generator Comprehension**: 
- Generator comprehensions are also very similar to lists with the variation of using curved brackets instead of square brackets. 
- They are also more memory efficient as compared to list comprehensions.
```
<class 'generator'> 
2 3 5 7 11 13 17 19 23 29 31 
```
In the code above, I created a generator object of the class generator instead of a list. 
- The elements in this iterator object cannot be directly accessed and need the help of a for loop and as such, I iterate over these elements and print them.

### List comprehension vs map() function:
```
def square(num):
    return num * 2

newdata = map(square, data)

newdata = [x + 3 for x in data] 
```
- Notice how both map() functions and list comprehension effectively do the same job of modifying iterator sequences such as the list in the example above.
- List comprehensions provide direct return of a list as compared to map() function that returns a map object. It is mainly the clarity that has made list comprehensions popular, but map() functions are still arguably a better choice when it comes to the use of larger sequences.

### Virtual environments
- Use venvs to isolate project packages from the system-wide Python packages
- Create virtual environment:
```
python -m venv .venv
```
- activate virtual environment (mac):
```
source .venv/bin/activate
```

### Sources: 

- Python built-in functions: https://docs.python.org/3/library/functions.html

- Python W3School: very good source to practice or find solutions
https://www.w3schools.com/python/

- HackerRank: https://www.hackerrank.com/domains/python

- LeetCode: https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=wpr69ksr

- RunStone Academy: Python Problem Solving and Data Structures
https://runestone.academy/ns/books/published/pythonds/index.html

- More On Data Structures:<br>
https://realpython.com/python-data-structures/ <br>
    Lists: https://docs.python.org/3/tutorial/datastructures.html

- Modules, packages, libraries: <br>
https://www.digitalocean.com/community/tutorials/how-to-import-modules-in-python-3

- Packages: 
https://realpython.com/python-modules-packages/#python-packages

- Testing: <br>
https://testdriven.io/blog/modern-tdd/ <br>
https://stackabuse.com/test-driven-development-with-pytest/ <br>
https://docs.pytest.org/en/7.1.x/ <br>
https://www.geeksforgeeks.org/python/best-python-modules-for-automation/

- BigO Notations:
https://dev.to/sarah_chima/the-big-o-notation-an-introduction-34f7

- Different types of algorithms used in Python:
https://www.thetechplatform.com/post/different-types-of-algorithms-in-data-structure

- Functional programming:
https://stackabuse.com/functional-programming-in-python/

- List comprehension:
https://www.upgrad.com/blog/python-list-comprehension/

- Recursion:
https://realpython.com/python-recursion/


# TODO
- check lambda functions
- at least 3 Python project to practice
- Python quizes on RealPython 
- RunStone Academy - a lot of small tasks, seems to be very good for practice




