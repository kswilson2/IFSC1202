#conversion chart given
#search first row for "from" unit
#search first column for "to" unit
#convert to floating point for everything except first row and column
#similar to project
FromValue = int(input("Enter From Value: "))
FromUnit = input("Enter From Unit (mm, cm, m, km, in, yd, mi): ")
ToUnit = input("Enter To Unit (mm, cm, m, km, in, yd, mi): ")
a = []
inputfile = open("09.04 Conversion.txt")
x = inputfile.readline()
while x != "":
	y = x.split(",")
	a.append(y) 
	x = inputfile.readline()
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()