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



### Sources: 

- Python built-in functions: https://docs.python.org/3/library/functions.html

- Python W3School: very good source to practice or find solutions
https://www.w3schools.com/python/

- HackerRank: https://www.hackerrank.com/domains/python

# TODO
- at least 3 Python project to practice
- Python quizes on RealPython 



