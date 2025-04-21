# Step 1 - Define the class object 
class RetailItem():
	
# Step 2 - Define the initializer and any default values
	def __init__(self, description="", units=0, price=0):
 
# Step 3 - Define the object attributes 
	    self.Description = description
		self.UnitsOnHand = units
		self.Price = price 
 
# Step 4 - Define Actions (Methods) associated with the object
	def Circumference(self):
		circumference =  pi * self.Diameter
		return circumference
 
# Step 4 - Here is another action
	def ChangePressure(self, pressurechange):
		self.Pressure += pressurechange
		return self.Pressure