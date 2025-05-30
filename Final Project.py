class Sketch:
    def __init__(self, size):
        self.size = size
        self.xpos = 0
        self.ypos = 0
        self.direction = 'U'  
        self.pen = 'U'  
        self.canvas = [[' ' for i in range(size)] for i in range(size)]  

    def printsketch(self):
        print('+', '-' * self.size, '+')
        for row in reversed(self.canvas):
            print('|', ''.join(row), '|')
        print('+', '-' * self.size, '+')
        print(f'X = {self.xpos} Y = {self.ypos} Direction = {self.direction}')

    def penup(self):
        self.pen = 'U'

    def pendown(self):
        self.pen = 'D'
        
    def turnleft(self):
        if self.direction == 'U':
            self.direction = 'R'
        elif self.direction == 'R':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'L'
        elif self.direction == 'L':
            self.direction = 'U'

    def turnright(self):
        if self.direction == 'U':
            self.direction = 'L'
        elif self.direction == 'L':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'R'
        elif self.direction == 'R':
            self.direction = 'U'

    def move(self, distance):
        for i in range(distance):
            if self.pen == 'D':
                self.canvas[self.xpos][self.ypos] = '*'
            if self.direction == 'U' and self.xpos < self.size - 1:
                self.xpos += 1
            elif self.direction == 'D' and self.xpos > 0:
                self.xpos -= 1
            elif self.direction == 'L' and self.ypos > 0:
                self.ypos -= 1
            elif self.direction == 'R' and self.ypos < self.size - 1:
                self.ypos += 1
                
with open("Cshape.txt", "r") as file:
    commands = file.read().splitlines()

sketch = Sketch(int(commands[0]))

for command in commands[1:]:
    action, *args = command.split(',')
    if action == '6':
        sketch.printsketch()
    elif action == '1':
        sketch.penup()
    elif action == '2':
        sketch.pendown()
    elif action == '3':
        sketch.turnleft()
    elif action == '4':
        sketch.turnright()
    elif action == '5':
        sketch.move(int(args[0]))