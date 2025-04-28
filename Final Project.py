class Sketch ():
	def __init__(self, size):
		self.size = size
		self.xpos = 0
		self.ypos = 0
		self.direction = "U"
		self.pen = "U"
		self.canvas = [[" " for i in range(size)] for i in range(size)]
	
    def printsketch(self):
        for i in range(size, -1):

    def penup(self):
		self.pen = "U"

    def pendown(self):
		self.pen = "D"

    def turnleft(self):
		if self.direction == "U":
			self.direction == "L"
		if self.direction == "L":
			self.direction == "D"
		if self.direction == "D":
			self.direction == "R"
		if self.direction == "R":
			self.direction == "U"

    def turnright(self):
		if self.direction == "U":
			self.direction == "R"
		if self.direction == "R":
			self.direction == "D"
		if self.direction == "D":
			self.direction == "L"
		if self.direction == "L":
			self.direction == "U"

    def move(self, distance):
	    for i in range(distance):
			
        if self.direction == "D":
			print("*")