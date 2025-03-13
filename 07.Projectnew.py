inputfile = open("07.Project Angles Input.txt", "r")
outputfile = open("07.Project Angles Output.txt", "w")
outputcount = 0
read = inputfile.read()
while read != "":
    degreeloc = read.find(chr(176))
    minuteloc = read.find("'")
    secondloc = read.find('"')
    degrees = float(read[:degreeloc])
    minutes = float(read[degreeloc+1:minuteloc])
    seconds = float(read[minuteloc+1:secondloc])
    decimaldegrees= degrees + (minutes/60) + (seconds/3600)
    break
    print(decimaldegrees) 