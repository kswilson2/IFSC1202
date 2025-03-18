n = input("Enter Values Separated by Spaces:")
a = []
s = n.split()
for x in range(len(s)):
    a.append(int(s[x]))
max= a[0] #assume 1st number is max
maxind = 0
for i in range(1, len(a)): #find max
    if a[i] > max: 
        max = a[i]
        maxind = i
print(maxind)
min= a[0]
minind = 0
for i in range(1, len(a)): #find min
    if a[i] < max: 
        min = a[i]
        minind = i
print(minind)
temp = a[minind]
a[minind] = a[maxind]
a[maxind] = temp
print(a)
#formatting trouble