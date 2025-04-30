#try type and perimeter only first. before area and angle.
import math 

class Triangle ():
	def __init__(self, side1, side2, side3):
		self.s1 = float(side1)
		self.s2 = float(side2)
		self.s3 = float(side3)
	def type(self):
		if (self.s1 == self.s2 == self.s3):
			return "Equilateral"
		elif (self.s1 == self.s2) or (self.s1 == self.s3) or (self.s2 == self.s3):
			return "Isosceles"
		else:
			return "Scalene"
	def perimeter(self):
		return self.s1 + self.s2 + self.s3
	def area(self):
		s = ((self.s1 + self.s2 + self.s3) / (2))
		area = math.sqrt(s*(s-self.s1)*(s-self.s2)*(s-self.s3))
		return (area)
	
    def angles(self):
        if(self.type()=="Equilateral"):
            return [60,60,60]
        elif(self.type()=="Isocelese"):
            b = 0.00
            if(self.side1==self.side2):
                b=self.side3
                h = math.sqrt(math.pow(self.side1,2) - math.pow(b/2,2))
                angle1 = (math.acos((b/2 * b/2 + self.side1 * self.side1 - h * h) / (b * self.side1))) * 180 / PI;
                angle2 = angle1
                angle3 = 180 - angle1 - angle2
                return [angle1, angle2, angle3]    
            elif(self.side2==self.side3):
                b=self.side1
                h = math.sqrt(math.pow(self.side2,2) - math.pow(b/2,2))
                angle1 = (math.acos((b/2 * b/2 + self.side2 * self.side2 - h * h) / (b * self.side2))) * 180 / PI;
                angle2 = angle1
                angle3 = 180 - angle1 - angle2
                return [angle1, angle2, angle3]
            else:
                b=self.side2
                h = math.sqrt(math.pow(self.side1,2) - math.pow(b/2,2))
                angle1 = (math.acos((b/2 * b/2 + self.side1 * self.side1 - h * h) / (b * self.side1))) * 180 / PI;
                angle2 = angle1
                angle3 = 180 - angle1 - angle2
                return [angle1, angle2, angle3]
                return 
            
        else:
            b = self.side3
            h = 2*(self.area()/b)
            a1 = math.sqrt(math.pow(self.side1,2) - math.pow(h,2))
            a2 = b-a1
            angle1 = (math.acos((a1 * a1 + self.side1 * self.side1 - h * h) / (2 * a1 * self.side1))) * 180 / PI;
            angle2 = (math.acos((a2 * a2 + self.side2 * self.side2 - h * h) / (2 * a2 * self.side2))) * 180 / PI;
            angle3 = 180-angle1-angle2
            return [angle2, angle1, angle3]
            
        
inputfile = open("Exam Three Triangle.txt", "r")
TriangleList = [] 
for x in inputfile:
    y = x.split(',')
    side1 = float(y[0])
    side2 = float(y[1])
    side3 = float(y[2])
    TriangleList.append(Triangle(side1,side2,side3))
inputfile.close()

print('{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}'.format('Type', 'Side 1', 'Side 2', 'Side 3', 'Perimeter',
													 'Area', 'Angle 1'))

for t in TriangleList:
	print('{:>12}{:>12}{:>12}{:>12}{:>12}{:>12.4}{:>12.4}'.format(t.type(), t.s1, t.s2, t.s3, t.perimeter(), t.area(), t.angle()))

	


	