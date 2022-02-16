from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.draw(STARTING_POSITION, 0.75, 0.75)

    def move_up(self):
        self.setheading(90)
        self.fd(10)

    def move_down(self):
        self.setheading(270)
        self.fd(10)

    def reset(self):
        super().reset()
        self.__init__()

    def draw(self, pos, width, length):
        self.penup()
        self.shapesize(stretch_wid=width, stretch_len=length)
        self.setheading(90)
        self.shape("turtle")
        self.setpos(pos)