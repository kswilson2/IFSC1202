#final
ddmmss = str(input("Enter: "))
degreeloc = ddmmss.find(chr(176))
minuteloc = ddmmss.find("'")
secondloc = ddmmss.find('"')
degrees = float(ddmmss[:degreeloc])
minutes = float(ddmmss[degreeloc+1:minuteloc])
seconds = float(ddmmss[minuteloc+1:secondloc])
decimaldegrees= degrees + (minutes/60) + (seconds/3600)
print(decimaldegrees)

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
