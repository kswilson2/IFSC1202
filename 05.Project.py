x = int(input("Enter Start of Range:"))
y = int(input("Enter End of Range: "))
for i in range(x, y+1):
    length = 0
    sum = 0
    original = i
    while i > 0:
        i //= 10
        length += 1
    while i > 0:
        digit = i % 10
        sum += digit ** length
        i //= 10
    if sum == original:
        print(original)