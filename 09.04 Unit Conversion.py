#conversion chart given
#search first row for "from" unit
#search first column for "to" unit
#convert to floating point for everything except first row and column
#similar to project
FromValue = float(input("Enter From Value: "))
FromUnit = input("Enter From Unit (mm, cm, m, km, in, yd, mi): ")
ToUnit = input("Enter To Unit (mm, cm, m, km, in, yd, mi): ")
a = []
inputfile = open("09.04 Conversion.txt")
x = inputfile.readline()
while x != "":
	y = x.split(" ")
	#for i in range(1, len(y)):
	#	    y[i] = float(y[i])
	a.append(y) 
	x = inputfile.readline()

FromIndex = -1
for i in range(len(a)):
	if a[i][0] == FromUnit: 
		FromIndex = i
if FromIndex == -1:
    print("FromUnit is not valid")
ToIndex = -1
for i in range(len(a[0])):
	if a[0][i] == ToUnit:
		ToIndex = i
if ToIndex == -1:
    print("ToUnit is not valid")
result = round(FromValue * a[FromIndex][ToIndex],7)
print(result)

	
		
    