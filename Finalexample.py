class Sketch:
    def __init__(self, size):
        # Initialize the Sketch object with the specified size.
        self.size = size
        self.xpos = 0
        self.ypos = 0
        self.direction = 'U'  # Initial direction: Up
        self.pen = 'U'  # Initial pen state: Up
        self.canvas = [[' ' for _ in range(size)] for _ in range(size)]  # Create a 2D canvas filled with spaces.

    def printsketch(self):
        # Print the sketch, including the canvas and current position/direction.
        print('+', '-' * self.size, '+')
        for row in reversed(self.canvas):
            print('|', ''.join(row), '|')
        print('+', '-' * self.size, '+')
        print(f'X = {self.xpos} Y = {self.ypos} Direction = {self.direction}')

    def penup(self):
        # Lift the pen up.
        self.pen = 'U'

    def pendown(self):
        # Put the pen down.
        self.pen = 'D'

    def turnright(self):
        # Turn the pen 90 degrees to the right.
        # The direction changes in a clockwise manner (U -> L -> D -> R -> U).
        if self.direction == 'U':
            self.direction = 'L'
        elif self.direction == 'L':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'R'
        elif self.direction == 'R':
            self.direction = 'U'

    def turnleft(self):
        # Turn the pen 90 degrees to the left.
        # The direction changes in a counter-clockwise manner (U -> R -> D -> L -> U).
        if self.direction == 'U':
            self.direction = 'R'
        elif self.direction == 'R':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'L'
        elif self.direction == 'L':
            self.direction = 'U'

    def move(self, distance):
        # Move the pen in the current direction for the specified distance.
        for _ in range(distance):
            if self.pen == 'D':
                # Draw '*' on the canvas if the pen is down.
                self.canvas[self.xpos][self.ypos] = '*'
            # Update the position based on the current direction.
            if self.direction == 'U' and self.xpos < self.size - 1:
                self.xpos += 1
            elif self.direction == 'D' and self.xpos > 0:
                self.xpos -= 1
            elif self.direction == 'L' and self.ypos > 0:
                self.ypos -= 1
            elif self.direction == 'R' and self.ypos < self.size - 1:
                self.ypos += 1
                
# Read commands from the file
with open("Cshape.txt", "r") as file:
    # Split the lines of the file into a list of commands
    commands = file.read().splitlines()

# Create and execute the Sketch object
sketch = Sketch(int(commands[0]))

# Iterate through the commands and perform corresponding actions on the Sketch object
for command in commands[1:]:
    # Split the command into action and arguments
    action, *args = command.split(',')
    
    # Check the action and execute the corresponding method on the Sketch object
    if action == '6':
        # Print the current state of the sketch
        sketch.printsketch()
    elif action == '1':
        # Lift the pen up
        sketch.penup()
    elif action == '2':
        # Put the pen down
        sketch.pendown()
    elif action == '3':
        # Turn the pen 90 degrees to the left
        sketch.turnleft()
    elif action == '4':
        # Turn the pen 90 degrees to the right
        sketch.turnright()
    elif action == '5':
        # Move the pen in the current direction by the specified distance
        sketch.move(int(args[0]))