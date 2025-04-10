#read, split by comma, just printing values

# Step 1 - Define the class object
class Pet ():
# Step 2 - Define the initializer and any default values
	def __init__(self):
# Step 3 - Define the object attributes
		self.Name = ""
		self.Type = ""
		self.Age = 0
#open input file to read
inputfile = open("10.01 Pets.txt","r")
#create list for objects
pets = []

