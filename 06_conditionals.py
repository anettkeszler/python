# LOGICAL OPERATORS
# and, or, not

a = True
b = True

if a and b:
    print("All True!")


a = True
b = False

if a or b:
    print("At least one is True")

a = True
b = False

if not(a) or not(b):
    print("All true!")


# CONDITIONAL STATEMENTS: 
bill_total = 210
discount1 = 10
discount2 = 20

if bill_total > 100 and bill_total < 200:
    bill_total = bill_total - discount1
    print("Bill is greater than 100.")
elif bill_total > 200:
    bill_total = bill_total - discount2
    print("Bill is greater than 200.")
else:
    print("Bill is less than 100.")

print(f"Total bill is {bill_total}")


# Light switch example
# Light is currently off
current = False

if current:
    current = False
    print("Turning light off.")
else:
    current = True
    print("Turning light on.")


# another example
loyalty_customer = True
total_bill = 120

if loyalty_customer and total_bill > 100:
    total_bill = total_bill - (float(total_bill) / 100) * 20
elif total_bill > 100:
    total_bill = total_bill - (float(total_bill) / 100)* 10
else:
    print("Sorry, no discount!")
print(f"Total bill is {float(total_bill)}")

# MATCH STATEMENT 
http_status = 500

match http_status:
    case 200 | 201:
        print("Success")
    case 400 :
        print("Bad Request")
    case 500 | 501:
        print("Server Error")
    case _:
        print("Unknown.")




