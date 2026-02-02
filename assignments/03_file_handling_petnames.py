"""
Imagine you are trying to come up with a name for your new dog. 
You're really unsure of what you'd like to call the dog, so you decide to use your Python skills to help you decide.

Create a program to choose a random petname from a given text file.

03_petnames.txt
"""
import random

file_name = "assignments/03_petnames.txt"

with open(file_name, 'r') as file:
    content = file.read()
    content_list = content.split("\n")
    random_name = random.choice(content_list)
    print(random_name)
   
