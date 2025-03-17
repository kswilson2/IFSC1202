n = input("Enter Values Separated by Spaces:")
a = []
s = n.split()
for i in range(1, len(s)):
    if s[i] > s[i-1]:
        print(s[i])