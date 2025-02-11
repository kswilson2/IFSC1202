first = int(input("Enter First Number: "))
second = int(input("Enter Second Number: "))
third = int(input("Enter Third Number: "))
if first <= second and first <= third:
    smallest = first
elif second <= first and second <= third:
    smallest = second
else:
    smallest = third
print(smallest)