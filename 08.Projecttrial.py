a = []
inputfile = open("constitution.txt", "r")
line = inputfile.readline()
prompt = input("Enter search term: ")
while line != "":
	a.append(line)
	line = inputfile.readline()
	strippedtext = line.strip('\n')
while strippedtext != "":
    find = strippedtext.find(prompt)
	if find != -1:
		print(find)
inputfile.close()