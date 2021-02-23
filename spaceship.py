from turtle import Turtle
from laser import Laser

INITIAL_PADDLE_SIZE = 20
SPACESHIP_IMG = "icons/spaceship_small.gif"
SPACESHIP_WIDTH = 100
SPACESHIP_HEIGHT = 20
X_POS = 0
Y_POS = -410
MOVE_INCREMENT = 20


class Spaceship(Turtle):
    def __init__(self, spaceship_img):
        super().__init__()
        self.shape(spaceship_img)
        # self.shapesize(stretch_wid=PADDLE_HEIGHT/INITIAL_PADDLE_SIZE, stretch_len=SPACESHIP_WIDTH / INITIAL_PADDLE_SIZE)
        # self.fillcolor("white")
        self.penup()
        # Position Spaceship
        self.goto(x=X_POS, y=Y_POS)
        self.set_spaceship_ends()

    def set_spaceship_ends(self):
        self.spaceship_left_x = self.xcor() - self.shapesize()[1] * INITIAL_PADDLE_SIZE / 2
        self.spaceship_right_x = self.xcor() + self.shapesize()[1] * INITIAL_PADDLE_SIZE / 2
        self.spaceship_inside_y = self.ycor() + self.shapesize()[0] * INITIAL_PADDLE_SIZE / 2
        self.spaceship_outside_y = self.ycor() - self.shapesize()[0] * INITIAL_PADDLE_SIZE / 2
        self.location = [(self.spaceship_left_x, self.spaceship_right_x), (self.spaceship_outside_y, self.spaceship_inside_y)]
        self.laser_turret_position = (self.xcor(), self.spaceship_inside_y)

    def move_left(self):
        if not self.spaceship_left_x - MOVE_INCREMENT < self.getscreen().window_width() / 2 * -1:
            self.goto(x=self.xcor() - MOVE_INCREMENT, y=self.ycor())
            self.set_spaceship_ends()

    def move_right(self):
        if not self.spaceship_right_x + MOVE_INCREMENT > self.getscreen().window_width() / 2:
            self.goto(x=self.xcor() + MOVE_INCREMENT, y=self.ycor())
            self.set_spaceship_ends()

    def shoot_laser(self):
        return Laser(self.laser_turret_position, "Up")


    def reset_game(self):
        # Position Spaceship
        self.goto(x=X_POS, y=Y_POS)
        self.set_spaceship_ends()