inputfile = open("06.Project Input File.txt", "r")
outputfile = open("06.Project Output File.txt", "w")
inputcount = 0
mergecount = 0
insert = "**Insert Merge File Here**"
line = inputfile.readline()
while line != "":
    if insert in line:
        break  
    outputfile.write(line)
    inputcount += 1
    line = inputfile.readline()
mergefile = open("06.Project Merge File.txt", "r")   
mergeline = mergefile.readline()
while mergeline != "":
    outputfile.write(mergeline)
    mergecount += 1
    mergeline = mergefile.readline()
while line != '':
    outputfile.write(line)
    inputcount += 1
    line = inputfile.readline()
inputfile.close()
outputfile.close()
print("{} input file records".format(inputcount))
print("{} merge file records".format(mergecount))
outputcount = inputcount + mergecount
print("{} output file records".format(outputcount))