n = input("Enter Values Separated by Spaces:")
a = []
s = n.split()
for x in range(len(s)):
    a.append(int(s[x]))
for x in range(len(s)):
       if a[x] % 2:
        print(a[x]) 