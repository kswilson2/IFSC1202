n = input("Enter Values Separated by Spaces:")
a = []
s = n.split()
for x in range(len(s)):
    a.append(int(s[x]))
for x in range(1, len(s),2):
    print(a[x])
#why is it printing 5 times 