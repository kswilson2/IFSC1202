import math
r = int(input("Enter Radius of Sphere: "))
y1 = float(input("Starting Point - Enter Latitude: "))
x1 = float(input("Starting Point - Enter Longitude: "))
y2 = float(input("Ending Point - Enter Latitude: "))
x2 = float(input("Ending Point - Enter Longitude: "))
y1rad = (y1*math.pi)/180
x1rad = (x1*math.pi)/180
y2rad = (y2*math.pi)/180
x2rad = (x2*math.pi)/180
d = r * math.acos(math.sin(y1rad)*math.sin(y2rad)+math.cos(y1rad)*math.cos(y2rad)*math.cos(x1rad-x2rad))
round = round(d,2)
print(f"The Great Circle Distance is {round}")
