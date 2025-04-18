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
#read file and add data
def main():
    inputfile = '10.Project Student Scores.txt' 
    list = []
    with open(inputfile, 'r') as file:
        for x in file:
            y = x.strip().split(',')
            s = Student(y[0], y[1], y[2], y[3:])
            list.append(s)
#print header
    print('{:>12}{:>12}{:>12}{:>14}{:>14}{:>12}'.format('First', 'Last', 'ID', 'Running', 'Semester', 'Letter'))
    print('{:>12}{:>12}{:>12}{:>14}{:>14}{:>12}'.format('Name', 'Name', 'Number', 'Average', 'Average', 'Grade'))
    print("------------ "*6)
#print data
    for std in list:
        print('{:>12}{:>12}{:>12}{:>14.2f}{:>14.2f}{:>12}'.format(std.FirstName, std.LastName, std.TNumber, std.TotalAverage(),std.RunningAverage(), std.LetterGrade()))
main()
 
