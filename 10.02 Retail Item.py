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
 
#open input file to read
inputfile = open("10.02 Inventory.txt")
#create list for objects
list = []
#read file
for i in inputfile:
	line = i.replace("\n","")
	data = line.split(",")
#store data
	temp = RetailItem() 
	temp.Description = data[0]
	temp.UnitsOnHand = int(data[1]) 
	temp.Price = float(data[2]) 
	list.append(temp)

#print header
print("{:>15} {:>10} {:>10} {:>15} ".format("Description","Units On Hand","Price","Inventory Value"))

#print data
for obj in list:
  print("{:>15} {:>10} {:>10} {:>15} ".format(obj.Description,obj.UnitsOnHand,obj.Price))

#close file
inputfile.close()