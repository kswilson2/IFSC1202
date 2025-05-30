def ParseDegreeString(ddmmss):
    degreeloc = ddmmss.find(chr(176))
    minuteloc = ddmmss.find("'")
    secondloc = ddmmss.find('"')
    degrees = float(ddmmss[:degreeloc])
    minutes = float(ddmmss[degreeloc+1:minuteloc])
    seconds = float(ddmmss[minuteloc+1:secondloc])
    return degrees, minutes, seconds
def DDMMSStoDecimal(degrees, minutes, seconds):
    decimaldegrees= degrees + (minutes/60) + (seconds/3600)
    return decimaldegrees

inputfile = open("07.Project Angles Input.txt", "r")
outputfile = open("07.Project Angles Output.txt", "w")
inputcount = 0
line = inputfile.readline()
while line != "":  
    degrees, minutes, seconds = ParseDegreeString(line) 
    decimaldegrees = DDMMSStoDecimal(degrees, minutes, seconds)
    outputfile.write(str(decimaldegrees) + "\n")
    inputcount += 1
    line = inputfile.readline()
inputfile.close()
outputfile.close()
print(inputcount,"records read")