#read, split by comma, just printing values

# Step 1 - Define the class object
class Pet ():
	
# Step 2 - Define the initializer and any default values
	def __init__(self, name, type, age):
 
# Step 3 - Define the object attributes
		self.Name = name
		self.Type = type
		self.Age = age 

#open input file to read
inputfile = open("10.01 Pets.txt", "r")
#create list for objects
a = []
line = inputfile.readline()
while line != "":
	line = line.strip()
	a.append(line)
	line = inputfile.readline()



