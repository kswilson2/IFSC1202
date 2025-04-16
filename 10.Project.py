# Step 1 - Define the class object 
class Student ():
# Step 2 - Define the initializer and any default values
	def __init__(self, firstname, lastname, tnumber, scores):
# Step 3 - Define the object attributes
		self.FirstName = firstname
		self.LastName = lastname
		self.TNumber = tnumber
		self.Grades = scores
# Step 4 - Define Actions (Methods) associated with the object
	def RunningAverage(self):
		scores = []
		for grade in self.Grades:
			if grade != "":
				scores.append(int(grade))
			else:
				scores.append(0)
		return sum(scores)/ len(scores)
# Step 4 - Here is another action
	def TotalAverage(self):
		scores = []
		for grade in self.Grades:
			if grade != "":
				scores.append(int(grade))
		return sum(scores)/ len(scores)		
# Step 4 - Here is another action
	def LetterGrade(self):
		average = self.RunningAverage
		if average >= 90:
			return "A"
		elif average >= 80:
			return "B"
		elif average >= 70:
			return "C"
		elif average >= 60:
			return "D"
		else:
			return "F"

inputfile = open("10.Project Student Scores.txt","r")
x = inputfile.readline()
list = []
while x != "":
	y = x.split(",")
	y[2]=y[2].strip()
	list.append(y) 
	x = inputfile.readline()
	student1 = Student(x[0], x[1], x[2], x[3:])
#print header
print("{:>10} {:>10} {:>10} {:>15} {:>15} {:>10}".format("First","Last","ID","Running","Semester","Letter"))
print("{:>10} {:>10} {:>10} {:>15} {:>15} {:>10}".format("Name","Name","Number","Average","Average","Grade"))
print("------------ "*6)
#print data
print(student1)
#close file
inputfile.close()
		
 
