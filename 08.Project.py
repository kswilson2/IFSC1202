#if line contains "liquor," go backwards to find blank and after to find blank
#line number will be index
a = []
inputfile = open("constitution.txt", "r")
x = inputfile.readline()
while x != "":
	a.append(x)
	x = inputfile.readline()
inputfile.close()
# Print the list - get the number of elements using the len() method
for i in range(len(a)):
	print(a[i])