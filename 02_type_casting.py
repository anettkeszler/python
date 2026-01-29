# TYPE CONVERSION
print(10 == 10)     # True

print(10 == 10.0)   # True - implicit type conversion, same numbers but not the same datatypes (int and float)

# when Python runs operations involving integers and floats, it implicitly converts the integers type to a float, and then completes the operation
print(10 + 10.0)    # 20.0 

print(type(10 + 10.0)) # <class 'float'> , implicit type conversion
