n = input("Enter Values Separated by Spaces:")
s = n.split()
a = []
distinct = 0
for i in range(len(a)):
    if a[i] != a[i+1]:
        distinct += 1
print(distinct)