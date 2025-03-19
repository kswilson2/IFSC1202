#if line contains "liquor," go backwards to find blank and after to find blank
#line number will be index
a = []
inputfile = open("constitution.txt", "r")
line = inputfile.readline()
prompt = input("Enter search term: ")
while line != "":
	a.append(line)
	line = inputfile.readline()
	strippedtext = line.strip('\n')
	find = strippedtext.find(prompt)
	if find != -1:
		print(find)

for i in range(1, find-1):
	firstblank = strippedtext.rfind("")
	print(firstblank)

for i in range (find+1):
	lastblank = strippedtext.find("")
	print(lastblank)
print(strippedtext[firstblank:lastblank])
inputfile.close()
		
