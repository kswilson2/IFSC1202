import math
import decimal
PI = 3.1415926535
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def type(self):
        if(self.side1==self.side2 and self.side2==self.side3):
            return "Equilateral"
        elif(self.side1==self.side2 or self.side2==self.side3 or self.side3==self.side1):
            return "Isocelese"
        else:
            return "Scalene"
            
    def perimeter(self):
        return self.side1+self.side2+self.side3
        
    def area(self):
        if(self.type()=="Equilateral"):
            return (math.sqrt(3)/ 4)*(self.side1 * self.side1)
        elif(self.type()=="Isocelese"):
            a=0.00
            b=0.00
            if(self.side1==self.side2):
                a=self.side1
                b=self.side3
            else:
                a=self.side1
                b=self.side2
            return (b * math.sqrt((4 * a * a) - (b * b)))/4
        else:
            s = self.perimeter() / 2  
            return (s*(s-self.side1)*(s-self.side2)*(s-self.side3)) ** 0.5 
            
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
            

TriangleList = []                    
inputfile = open("Exam Three Triangle.txt", "r")
for x in inputfile:
    vals = x.split(',')
    s1 = float(vals[0])
    s2 = float(vals[1])
    s3 = float(vals[2])
    TriangleList.append(Triangle(s1,s2,s3))


print(f"{'Type':20}{'Side 1':12}{'Side 2':12}{'Side 3':12}{'Perimeter':12}{'Area':8}{'Angle 1':13}{'Angle 2':12}{'Angle 3':12}")
for item in TriangleList:
    print(f"{item.type():12}{item.side1:12}{item.side2:12}{item.side3:12}{item.perimeter():12}{round(item.area(),3):12}{round(item.angles()[0],3):12}{round(item.angles()[1],3):12}{round(item.angles()[2],3):12}")
