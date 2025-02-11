first = float(input("Enter First Number: "))
operator = input("Enter Operator (+,-,*,/): ")
second = float(input("Enter Second Number: "))
if operator == "+":
    result = first + second
elif operator == "-":
    result = first - second
elif operator == "*":
    result = first * second
elif operator == "/":
    result = first / second
else:
    result = None
if result != None:
    print(f"{first} {operator} {second} = {result}")
else: 
   print("Invalid Operator")