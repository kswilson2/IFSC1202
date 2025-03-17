a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
#2 for loops needed to run through two dim list 
for i in range(len(a)): #number of lists
    for j in range(len(a[i])): #length of each list 
        s += a[i][j]
print("The sum is: {}".format(s))