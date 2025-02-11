first = int(input("Enter First Number: "))
second = int(input("Enter Second Number: "))
third = int(input("Enter Third Number: "))
if first == second and first == third:
    print(int(3))
elif first == second or first == third or second == third:
    print(int(2))
else:
    print(int(0))