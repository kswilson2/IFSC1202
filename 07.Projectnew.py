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
lines = inputfile.readlines()
filecount = 0
while lines != "":
    degreeloc = lines.find(chr(176))
    minuteloc = lines.find("'")
    secondloc = lines.find('"')
    degrees = float(lines[:degreeloc])
    minutes = float(lines[degreeloc+1:minuteloc])
    seconds = float(lines[minuteloc+1:secondloc])
    decimaldegrees= degrees + (minutes/60) + (seconds/3600)
    filecount += 1
    outputfile.write(f"{decimaldegrees}")
    print(filecount)