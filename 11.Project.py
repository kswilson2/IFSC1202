# Step 1 - Define the class object 
class Student ():
# Step 2 - Define the initializer
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
		average = self.RunningAverage()
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

# Step 1 - Define the class object 
class StudentList ():
	
# Step 2 - Define the initializer and any default values
	def __init__(self):
 
# Step 3 - Define the object attributes
		self.Studentlist = []
 
# Step 4 - Define Actions (Methods) associated with the object
# Add student to the list
	def add_student(self, FirstName="", LastName="", TNumber=""):
#		Create a new student object
		mystudent = Student(FirstName, LastName, TNumber)
#		Append student object to list
		self.Studentlist.append(mystudent)
		
# Find a student and return the index
	def find_student(self, studenttofind):
		for i in range(len(self.Studentlistlist)):
			if self.Studentlist[i].TNumber == studenttofind:
				return i
		return -1	
	
# Print the student list
	def print_student_list(self):
		print('{:>12}{:>12}{:>12}{:>14}{:>14}{:>12}'.format('First', 'Last', 'ID', 'Running', 'Semester', 'Letter'))
		for i in range(len(self.Studentlist)):
			print('{:>12}{:>12}{:>12}{:>14.2f}{:>14.2f}{:>12}'.format(self.Studentlist[i].FirstName, self.Studentlist[i].LastName, self.Studentlist[i].TNumber, self.Studentlist[i].TotalAverage, self.Studentlist[i].RunningAverage, elf.Studentlist[i].LetterGrade()))
		print()
		print("{} balls in list".format(self.number_of_balls()))
		print()
		
# Read a file and append the vales to the ball list
	def add_student_from_file(self, filename):
		studentfile = open(filename)
		x = studentfile.readline()
		while x != "":
#			print(x) # display what was read
			y = x.split(",")
#			print(y) # display the result of the split
			self.add_student(y[0].strip(), y[1].strip(), y[2].strip())
			x = studentfile.readline()
		studentfile.close()