inputfile = open("06.Project Input File.txt", "r")
outputfile = open("06.Project Output File.txt", "w")
recordcount = 0
line = inputfile.readline()
while line != " ":
    outputfile.write(line)
    recordcount += 1
    line = inputfile.readline()
inputfile.close()
outputfile.close()

