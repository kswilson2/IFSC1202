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
	
FromCity = input("Enter From City: ")
ToCity = input("Enter To City: ")

FromIndex = 0
for i in range(len(a)):
	if a[i][0] == FromCity: 
		FromIndex = i
if FromCity == -1:
    print("Invalid From City")	
ToIndex = 0
for i in range(len(a[0])):
	if a[0][i] == ToCity:
		ToIndex = i
if ToIndex == -1:
    print("Invalid To City")
if FromIndex != -1:
	print(FromIndex)
if ToIndex != -1:
	print(ToIndex)