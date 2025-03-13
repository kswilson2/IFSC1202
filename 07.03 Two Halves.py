s = str(input("Enter a string: "))
length = len(s)
split = (length + 1) // 2
strone = s[:split]
strtwo = s[split:]
print(strtwo + strone)
