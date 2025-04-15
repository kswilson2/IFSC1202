#make sure to do examples first

# Step 1 - Define the class object 
class Student ():
	
# Step 2 - Define the initializer and any default values
	def __init__(self, firstname, lastname, tnumber:
 
# Step 3 - Define the object attributes
		self.BallType = balltype 
		self.Diameter = diameter 
		self.Pressure = pressure 
 
# Step 4 - Define Actions (Methods) associated with the object
	def Circumference(self):
		circumference =  pi * self.Diameter
		return circumference
 
# Step 4 - Here is another action
	def ChangePressure(self, pressurechange):
		self.Pressure += pressurechange
		return self.Pressure
 
# Step 5 - Create 4 instances of ball
myball1 = Ball("Basketball", 9.51, 8.0)
myball2 = Ball("Volleyball", 8.15, 7.5)
myball3 = Ball("Soccerball", 8.65, 9.0)
myball4 = Ball() #basketball is assumed using default values