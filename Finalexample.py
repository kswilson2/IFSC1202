class Sketch:
    def __init__(self, size):
        self.size = size
        self.xpos = 0
        self.ypos = 0
        self.direction = 'U'  # Up
        self.pen = 'U'  # Up
        self.canvas = [[' ' for _ in range(size)] for _ in range(size)]

    def printsketch(self):
        print("\n")
        for i in range(self.size - 1, -1, -1):
            print("".join(self.canvas[i]))
        print("\n")
        print(f"X: {self.xpos}, Y: {self.ypos}, Direction: {self.direction}")

    def penup(self):
        self.pen = 'U'

    def pendown(self):
        self.pen = 'D'

    def turnleft(self):
        if self.direction == 'U':
            self.direction = 'L'
        elif self.direction == 'L':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'R'
        else:
            self.direction = 'U'

    def turnright(self):
        if self.direction == 'U':
            self.direction = 'R'
        elif self.direction == 'R':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'L'
        else:
            self.direction = 'U'

    def move(self, distance):
        for _ in range(distance):
            if self.direction == 'U':
                new_ypos = self.ypos - 1
                if 0 <= new_ypos < self.size:
                    if self.pen == 'D':
                        self.canvas[new_ypos][self.xpos] = '*'
                    self.ypos = new_ypos
                else:
                    break
            elif self.direction == 'D':
                new_ypos = self.ypos + 1
                if 0 <= new_ypos < self.size:
                    if self.pen == 'D':
                        self.canvas[new_ypos][self.xpos] = '*'
                    self.ypos = new_ypos
                else:
                    break
            elif self.direction == 'L':
                new_xpos = self.xpos - 1
                if 0 <= new_xpos < self.size:
                    if self.pen == 'D':
                        self.canvas[self.ypos][new_xpos] = '*'
                    self.xpos = new_xpos
                else:
                    break
            elif self.direction == 'R':
                new_xpos = self.xpos + 1
                if 0 <= new_xpos < self.size:
                    if self.pen == 'D':
                        self.canvas[self.ypos][new_xpos] = '*'
                    self.xpos = new_xpos
                else:
                    break


# Main execution
with open("Cshape.txt", "r") as file:
    size = int(file.readline().strip())
    sketch = Sketch(size)

    for line in file:
        command = line.strip().split(",")
        command_type = int(command[0])

        if command_type == 1:
            sketch.penup()
        elif command_type == 2:
            sketch.pendown()
        elif command_type == 3:
            sketch.turnright()
        elif command_type == 4:
            sketch.turnleft()
        elif command_type == 5:
            distance = int(command[1])
            sketch.move(distance)
        elif command_type == 6:
            sketch.printsketch()