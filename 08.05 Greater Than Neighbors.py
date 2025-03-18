n = input("Enter Values Separated by Spaces:")
a = []
s = n.split()
for x in range(len(s)):
    a.append(int(s[x]))
count = 0
for i in range(1, len(a)-1):
    if (a[i] > a[i-1] and a[i] > a[i+1]):
        count += 1
print(count)
 