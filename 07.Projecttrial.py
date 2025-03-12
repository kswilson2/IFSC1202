
degreeloc = read.find(chr(176))
minuteloc = read.find("'")
secondloc = read.find('"')
degrees = float[0:degreeloc]
minutes = float[degreeloc+1:minuteloc]
seconds = float[minuteloc+1:secondloc]

degrees = float[0:read.find(chr(176))]

minute = float(read.find("'"))
second = float(read.find('"'))
