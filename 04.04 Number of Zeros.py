N = int(input("Enter N:"))
zero = 0
for i in range(N):
    number = int(input("Enter Number: "))
    if number == 0:
        zero += 1
print(zero)