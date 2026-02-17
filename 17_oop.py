class MyClass:
    print("hello")
    a = 5

    def hello(self):
        print("Hello world!")

myclass = MyClass()

# instance reference  
print(myclass.a)
myclass.hello()

# class reference
print(MyClass.a)




class House:
    rooms = 5
    bathrooms = 2

    def cost_evaluation(self, rate):
        cost = rate * self.rooms
        return cost

house = House()
print(house.rooms)
print(House.rooms)

house.rooms = 7
print(house.rooms) # 7
print(House.rooms) # remain 5




value = 7
class A:
    value = 5
a = A()
a.value = 3
print(value) # 7





