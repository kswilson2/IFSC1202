class Student ():
	def __init__(self, firstname="", lastname="", tnumber=""):
		self.FirstName = firstname
		self.LastName = lastname
		self.TNumber = tnumber
		self.Grades = []
		
	def RunningAverage(self):
		scores = []
		for grade in self.Grades:
			if grade != "":
				scores.append(int(grade))
		return sum(scores)/ len(scores) 

	def TotalAverage(self):
		scores = []
		for grade in self.Grades:
			if grade != "":
				scores.append(int(grade))
			else:
				scores.append(0)
		return sum(scores)/len(scores)
# Step 4 - Here is another action
	def LetterGrade(self):
		average = self.TotalAverage()
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
		print('{:>12}{:>12}{:>12}{:>14}{:>14}{:>12}'.format('First', 'Last', 'ID', 'Running', 'Semester', 'Letter'))
		print('{:>12}{:>12}{:>12}{:>14}{:>14}{:>12}'.format('Name', 'Name', 'Number', 'Average', 'Average', 'Grade'))
		print("------------ "*6)
		for student in self.Studentlist:
			print('{:>12}{:>12}{:>12}{:>14.2f}{:>14.2f}{:>12}'.format(student.FirstName, student.LastName, student.TNumber,
                student.RunningAverage(), student.TotalAverage(), student.LetterGrade()))
# Read a file and append the values to the student list
	def add_student_from_file(self, filename):
		studentfile = open(filename, "r")
		x = studentfile.readline()
		while x != "":
			y = x.split(",")
			self.add_student(y[0].strip(), y[1].strip(), y[2].strip())
#		print(y) # display the result of the split
			x = studentfile.readline()
		studentfile.close()
# Read a file and append the values to the scores list
	def add_scores_from_file(self, filename):
		scoresfile = open(filename, "r")
		x = scoresfile.readline()
		while x != "":
			y = x.split(",")
#		print(y) # display the result of the split
			index = self.find_student(y[0].strip())
			if index != -1:
				for grade in y:
					self.Studentlist[index].Grades.append(y[1].strip())
			x = scoresfile.readline()
		scoresfile.close()

#--------------------------------------------------------------------
 
mystudentlist = StudentList()
 
# Read student List from File
mystudentlist.add_student_from_file("11.Project Students.txt")

# Read Scores List from File
mystudentlist.add_scores_from_file("11.Project Scores.txt")

# Display List
print()
mystudentlist.print_student_list()