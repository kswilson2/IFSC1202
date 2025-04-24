# Step 1 - Define the class object 
class Student ():
# Step 2 - Define the initializer
	def __init__(self, firstname="", lastname="", tnumber="", scores=[]):
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
		student = Student(FirstName, LastName, TNumber)
#		Append student object to list
		self.Studentlist.append(student)
		
# Find a student and return the index
	def find_student(self, studenttofind):
		for i in range(len(self.Studentlist)):
			if self.Studentlist[i].TNumber == studenttofind:
				return i
		return -1	
	
# Print the student list
	def print_student_list(self):
		for student in self.Studentlist:
			print(f"Name: {student.FirstName} {student.LastName}, TNumber: {student.TNumber}")
			print(f"  Running Average: {student.RunningAverage()}")
			print(f"  Total Average: {student.TotalAverage()}")
			print(f"  Letter Grade: {student.LetterGrade()}")
#		print('{:>12}{:>12}{:>12}{:>14}{:>14}{:>12}'.format('First', 'Last', 'ID', 'Running', 'Semester', 'Letter'))
#		for i in range(len(self.Studentlist)):
#			print('{:>12}{:>12}{:>12}{:>14.2f}{:>14.2f}{:>12}'.format(self.Studentlist[i].FirstName, self.Studentlist[i].LastName, self.Studentlist[i].TNumber, self.Studentlist[i].TotalAverage, self.Studentlist[i].RunningAverage, self.Studentlist[i].LetterGrade()))
#		for std in self.StudentList:
#			print('{:>12}{:>12}{:>12}{:>14.2f}{:>14.2f}{:>12}'.format(std.FirstName, std.LastName, std.TNumber, std.TotalAverage(),std.RunningAverage(), std.LetterGrade()))
#		print()
		
# Read a file and append the values to the student list
	def add_student_from_file(self, filename):
		studentfile = open(filename)
		x = studentfile.readline()
		while x != "":
			y = x.split(",")
#			print(y) # display the result of the split
			self.add_student(y[0].strip(), y[1].strip(), y[2].strip())
			x = studentfile.readline()
		studentfile.close()

# Read a file and append the values to the scores list
#	def add_scores_from_file(self, filename):
#		scoresfile = open(filename)
#		x = scoresfile.readline()
#		while x != "":
#			y = x.split(",")
#			print(y) # display the result of the split
#			self.add_student(y[0].strip(), y[1].strip())
#			x = scoresfile.readline()
#		scoresfile.close()


#--------------------------------------------------------------------
 
mystudentlist = StudentList()
 
# Read student List from File
mystudentlist.add_student_from_file("11.Project Students.txt")

# Read Scores List from File
#mystudentlist.add_scores_from_file("11.Project Scores.txt")

# Display List
print()
mystudentlist.print_student_list()


