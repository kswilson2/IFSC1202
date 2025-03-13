inputfile = open("07.Project Angles Input.txt", "r")
outputfile = open("07.Project Angles Output.txt", "w")
outputcount = 0
line = inputfile.readline()
while line != "":
    degreeloc = line.find(chr(176))
    minuteloc = line.find("'")
    secondloc = line.find('"')
    degrees = float(line[:degreeloc])
    minutes = float(line[degreeloc+1:minuteloc])
    seconds = float(line[minuteloc+1:secondloc])
    decimaldegrees= degrees + (minutes/60) + (seconds/3600)
    outputfile.write(str(decimaldegrees))
    outputcount += 1 
    break
inputfile.close()
outputfile.close()

    