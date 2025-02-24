x = int(input("Enter Start of Range:"))
y = int(input("Enter End of Range:"))
for i in range(x, y+1):
    original = i
    sum = 0
    n = len(str(i))
    while i > 0:
        digit = i % 10
        sum += digit ** n
        i //= 10
    if sum == original:
        print(original)