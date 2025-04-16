class RetailItem ():
	
# Step 2 - Define the initializer and any default values
	def __init__(self, description="", units=0, price=0):
 
# Step 3 - Define the object attributes
		self.Description = description
		self.UnitsOnHand = units
		self.Price = price 
 
# Step 4 - Define Actions (Methods) associated with the object
	def InventoryValue(self):
		inventoryvalue =  self.UnitsOnHand * self.Price
		return inventoryvalue
 
inputfile = open("10.01 Pets.txt","r")

# Step 5 - Create 4 instances of ball
myball1 = Ball("Basketball", 9.51, 8.0)
myball2 = Ball("Volleyball", 8.15, 7.5)
myball3 = Ball("Soccerball", 8.65, 9.0)
myball4 = Ball() #basketball is assumed using default values