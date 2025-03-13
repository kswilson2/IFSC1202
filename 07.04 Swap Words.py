s = str(input("Enter a string: "))
split = (s.find(' ')) + 1
print(s[split:] + " " + s[:split])