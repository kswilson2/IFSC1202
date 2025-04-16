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
#read file
for i in inputfile:
	line = i.replace("\n","")
	data = line.split(",")
#store data
	temp = Pet() 
	temp.Name = data[0]
	temp.Type = data[1]
	temp.Age = int(data[2])
	pets.append(temp)

#print header
print("{:>10} {:>10} {:>10} ".format("Name","Type","Age"))

#print data
for obj in pets:
  print("{:>10} {:>10} {:>10} ".format(obj.Name,obj.Type,obj.Age))

#close file
inputfile.close()