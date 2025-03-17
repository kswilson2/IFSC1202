n = input("Enter Values Separated by Spaces:")
a = []
s = n.split()
for x in range(len(s)):
    a.append(int(s[x]))
for x in range(len(s)):
    print(a[1], a[3])
#why is it printing 5 times 