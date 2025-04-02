a = []
inputfile = open("09.Project Distances.csv")
x = inputfile.readline()
while x != "":
	y = x.split(",")
	a.append(y) 
	x = inputfile.readline()
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()