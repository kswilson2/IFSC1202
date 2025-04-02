inputfile = open("Exam Two Names.txt", "r")
x = inputfile.readline()
a = []
while x != "":
	y = x.split(",")
	#y = x.strip()
	y[1]=y[1].strip()
	a.append(y) 
	x = inputfile.readline()
for i in range(len(a)):
    prompt = input("Enter a Name: ").strip().title()
    if prompt == "q".title():
	    exit()
    boyindex = 0
    for i in range(len(a)):
	    if a[i][0] == prompt: 
		    boyindex = i
    girlindex = 0
    for i in range(len(a)):
	    if a[i][1] == prompt: 
		    girlindex= i
    boyrank = int(boyindex + 1)
    girlrank = int(girlindex +1)
    if boyindex != 0:
	    print("Boy's Name - Rank: " ,boyrank)
    if girlindex != 0:
	    print("Girls's Name - Rank: " ,girlrank)
    if a[i][0] != prompt and a[i][1] != prompt:
	    print("Name Not Found")



	