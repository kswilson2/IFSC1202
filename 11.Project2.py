class Student ():
    def __init__(self, firstname="", lastname="", tnumber=""):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []
    def RunningAverage(self):
        valid_grades = [int(grade) for grade in self.Grades if grade.strip() != '']
        return sum(valid_grades) / len(valid_grades) if valid_grades else 0
    def TotalAverage(self):
        total_sum = sum(int(grade) if grade.strip() != '' else 0 for grade in self.Grades)
        return total_sum / len(self.Grades) if self.Grades else 0
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

class StudentList ():
	
	def __init__(self):
		self.Studentlist = []
		
	def add_student(self, FirstName="", LastName="", TNumber=""):
		student = Student(FirstName, LastName, TNumber)
		self.Studentlist.append(student)
		
	def find_student(self, studenttofind):
		for i in range(len(self.Studentlist)):
			if self.Studentlist[i].TNumber == studenttofind:
				return i
		return -1
	
	def print_student_list(self):
		for student in self.Studentlist:
			print(f"Name: {student.FirstName} {student.LastName}, TNumber: {student.TNumber}")
			print(f"  Running Average: {student.RunningAverage()}")
			print(f"  Total Average: {student.TotalAverage()}")
			print(f"  Letter Grade: {student.LetterGrade()}")
			
	def add_student_from_file(self, filename):
		studentfile = open(filename)
		x = studentfile.readline()
		while x != "":
			y = x.split(",")
			self.add_student(y[0].strip(), y[1].strip(), y[2].strip())
			x = studentfile.readline()
		studentfile.close()	
		
#--------------------------------------------------------------------
 
mystudentlist = StudentList()
 
# Read student List from File
mystudentlist.add_student_from_file("11.Project Students.txt")

# Read Scores List from File
#mystudentlist.add_scores_from_file("11.Project Scores.txt")

# Display List
print()
mystudentlist.print_student_list()

		
		

