n = input("Enter Values Separated by Spaces:")
a = []
s = n.split()
for x in range(len(s)):
    a.append(int(s[x]))
for i in range(1, len(a)-1):
    if (a[i] >= 0 and a[i+1] >= 0) or (a[i] < 0 and a[i+1] < 0):
        print(a[i], a[i+1])   