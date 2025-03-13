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

def file("07.Project Angles Input.txt","07.Project Angles Output.txt"):
    with open("07.Project Angles Input.txt", "r") as infile:
        lines = infile.readlines()
    outputcount = 0
    for line in lines:
        degrees, minutes, seconds = ParseDegreeString(ddmmss)
        decimaldegrees = DDMMSStoDecimal(degrees, minutes, seconds)
        outputcount += 1
    with open("07.Project Angles Output.txt", "w") as outfile:
        for decimaldegrees in outputcount:
        outputfile.write(f'{decimaldegrees}')
    return outputcount
line = inputfile.readline()
outputcount = 0 