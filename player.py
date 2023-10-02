from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.color('green')
        self.shapesize(stretch_wid=1, stretch_len=1)
    def move_up(self):
        y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), y)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
