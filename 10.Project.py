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

inputfile = open("10.Project Student Scores.txt")
x = inputfile.readline()
list = []
while x != "":
	y = x.split(",")
	y = x.replace("\n","")
	student = Student(y[0].strip(), (y[1].strip()), (y[2].strip()), (y[3].strip()))
	list.append(student)
	x = inputfile.readline()

#close file
inputfile.close()


#print header
#print("{:>10} {:>10} {:>10} {:>15} {:>15} {:>10}".format("First","Last","ID","Running","Semester","Letter"))
#print("{:>10} {:>10} {:>10} {:>15} {:>15} {:>10}".format("Name","Name","Number","Average","Average","Grade"))
#print("------------ "*6)
#print data

# for std in list:
#	print('{:>10}{:>10}{:>14}{:>15.2f}{:>15.2f}{:>10}'.format(std.FirstName, std.LastName, std.TNumber, std.TotalAverage(),std.RunningAverage(),std.LetterGrade()))

def main():
    filename = '10.Project Student Scores.txt' 
    stud_list = []
    with open(filename, 'r') as infile:
        for line in infile:
            line = line.strip().split(',')
            s = Student(line[0], line[1], line[2], line[3:])
            stud_list.append(s)

    print('{:>10}{:>10}{:>14}{:>15}{:>15}{:>10}'.format('First', 'Last', 'ID', 'Running', 'Semester', 'Letter'))
    print('{:>10}{:>10}{:>14}{:>15}{:>15}{:>10}'.format('Name', 'Name', 'Number', 'Average', 'Average', 'Grade'))
    print('-' * 75)
    for std in stud_list:
        print('{:>10}{:>10}{:>14}{:>15.2f}{:>15.2f}{:>10}'.format(std.FirstName, std.LastName, std.TNumber,
                                                                  std.TotalAverage(),std.RunningAverage(),
                                                            std.LetterGrade()))
main()	
 
