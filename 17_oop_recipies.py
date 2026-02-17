class Recipe:

    def __init__(self, dish, items, time):
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print("The " + self.dish + " has" + str(self.items) + " and takes " + str(self.time) + " min to prepare.")


pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipe("Pasta", ["penne", "sauce"], 55)

print(pizza.time)
print(pasta.items)
    
print(pizza.contents())


class Author():

    index = "Author-Book"

    # pass the print statement into constructor
    def __init__(self):
        print("Who wrote this?")

    def hand_list(self, philosopher, book):

        print(Author.index)
        print(philosopher + " wrote this book: " + book)

# instantiate the class
author = Author()
# call the method with parameters
print(author.hand_list("Jack London", "Singing Dog"))


# Instance methods
class Payslips():
    def __init__(self, name, payment, amount):
        self.name = name
        self.payment = payment
        self. amount = amount

    def pay(self):
        self.payment = "yes"
    
    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yet"
    
nathan = Payslips("Nathan", "no", 1000)
rodger = Payslips("Roger", "no", 3000)

print(nathan.status(), "\n", rodger.status())

nathan.pay()

print("After payment")

print(nathan.status(), "\n", rodger.status())

# Inheritance (Parent and child classes)
class Employees:
    def __init__(self, name, last):
        self.name = name
        self.last = last

class Supervisiors(Employees):
    def __init__(self, name, last, password):
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def __init__(self, name, last):
        super().__init__(name, last)

    def leave_request(self, days):
        return "May I take a leave for " + str(days) + " days?"

    
adrian = Supervisiors("Adrian", "A", "apple")

emily = Chefs("Emily", "E")
juno = Chefs("Juno", "J")

print(emily.leave_request(3))

print(adrian.password)
print(emily.name)