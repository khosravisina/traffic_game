from turtle import Turtle
FONT = ("Courier", 32, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(-150, 270)
        self.level = 1
        self.do_write()

    def do_write(self):
        self.write(arg=f'LEVEL {self.level}', font=("Courier", 14, "normal"), align='left')

    def updata_level(self):
        self.level += 1
        self.clear()
        self.do_write()

    def gave_over(self):
        self.clear()
        self.goto(0,0)
        self.write(arg='game over', font=FONT, align='center')