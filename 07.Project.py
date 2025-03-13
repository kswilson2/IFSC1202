inputfile = open("07.Project Angles Input.txt", "r")
read = inputfile.readline()
outputcount = 0
while read != "":
    degreeloc = read.find(chr(176))
    minuteloc = read.find("'")
    secondloc = read.find('"')
    degrees = float(read[:degreeloc])
    minutes = float(read[degreeloc+1:minuteloc])
    seconds = float(read[minuteloc+1:secondloc])
    decimaldegrees= degrees + (minutes/60) + (seconds/3600)
    outputfile = open("07.Project Angles Output.txt", "w")
    outputcount += 1
    outputfile.write(str(decimaldegrees))
    break
    print(outputcount)  
    
