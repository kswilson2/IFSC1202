#if line contains "liquor," go backwards to find blank and after to find blank
#line number will be index
a = []
inputfile = open("constitution.txt", "r")
x = inputfile.readline()
while x != "":
	a.append(x)
	x = inputfile.readline()
	strip = x.strip('\n') #not sure if strip is working 
inputfile.close()

prompt = input("Enter search term: ")
while x != "":
	find = x.find(prompt)
	if x 
	print(find)
		
