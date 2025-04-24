class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []

    def RunningAverage(self):
        """Calculates the running average of non-blank scores."""
        valid_grades = [int(grade) for grade in self.Grades if grade.strip() != '']
        return sum(valid_grades) / len(valid_grades) if valid_grades else 0

    def TotalAverage(self):
        """Calculates the average of scores, treating missing scores as zero."""
        total_sum = sum(int(grade) if grade.strip() != '' else 0 for grade in self.Grades)
        return total_sum / len(self.Grades) if self.Grades else 0

    def LetterGrade(self):
        """Returns the letter grade based on the TotalAverage."""
        average = self.TotalAverage()
        if average >= 90:
            return "A"
        elif 80 <= average < 90:
            return "B"
        elif 70 <= average < 80:
            return "C"
        elif 60 <= average < 70:
            return "D"
        else:
            return "F"

class StudentList:
    def __init__(self):
        self.Studentlist = []

    def add_student(self, firstname, lastname, tnumber):
        """Adds a student object to the Studentlist."""
        student = Student(firstname, lastname, tnumber)
        self.Studentlist.append(student)

    def find_student(self, tnumber):
        """Finds a student by TNumber and returns the index, or -1 if not found."""
        for index, student in enumerate(self.Studentlist):
            if student.TNumber == tnumber:
                return index
        return -1

    def print_student_list(self):
        """Prints the attributes of each student in the list."""
        for student in self.Studentlist:
            print(f"Name: {student.FirstName} {student.LastName}, TNumber: {student.TNumber}")
            print(f"  Running Average: {student.RunningAverage()}")
            print(f"  Total Average: {student.TotalAverage()}")
            print(f"  Letter Grade: {student.LetterGrade()}")
            print("-" * 20)

    def add_student_from_file(self, filename):
        """Reads student data from a file and adds them to the Studentlist."""
        try:
            with open(filename, "r") as file:
                for line in file:
                    firstname, lastname, tnumber = line.strip().split(",")
                    self.add_student(firstname, lastname, tnumber)
        except FileNotFoundError:
            print(f"Error: File not found: {filename}")

    def add_scores_from_file(self, filename):
        """Reads student scores from a file and adds them to the appropriate student object."""
        try:
            with open(filename, "r") as file:
                for line in file:
                    tnumber, *grades = line.strip().split(",")
                    student_index = self.find_student(tnumber)
                    if student_index != -1:
                        self.Studentlist[student_index].Grades.extend(grades)
                    else:
                        print(f"Warning: Student with TNumber {tnumber} not found.")
        except FileNotFoundError:
            print(f"Error: File not found: {filename}")

# Main Program
student_list = StudentList()

# Add students from file
student_list.add_student_from_file("11.Project Students.txt")

# Add scores from file
student_list.add_scores_from_file("11.Project Scores.txt")

# Print the student list
student_list.print_student_list()