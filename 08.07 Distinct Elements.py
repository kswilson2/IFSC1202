n = input("Enter Values Separated by Spaces:")
a = []
s = n.split()
for x in range(len(s)):
    a.append(int(s[x]))
distinct = 0
for i in range(len(a)-1):
    if a[i] != a[i+1]:
        distinct += 1
print(f'Number of Distinct Elements: {distinct}')
#why am I getting 2 instead of 3