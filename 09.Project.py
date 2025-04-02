a = []
inputfile = open("09.Project Distances.csv")
x = inputfile.readline()
while x != "":
	y = x.split(",")
	y[9]=y[9].strip()
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
if FromIndex == 0:
    print("Invalid From City")	
ToIndex = 0
for i in range(len(a[i])):
	if a[0][i] == ToCity:
		ToIndex = i
if ToIndex == 0:
    print("Invalid To City")
print(f'{FromCity} to {ToCity} - {a[FromIndex][ToIndex]} miles')