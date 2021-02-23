from turtle import Turtle, Screen
import random
from laser import Laser

INITIAL_SHAPE_SIZE = 20
INVADER_WIDTH = INITIAL_SHAPE_SIZE
INVADER_ICONS = ["invader_1.png", "invader_2.png", "invader_3.png"]
INVADER_ICONS_SMALL = ["icons/invader_1_small.gif", "icons/invader_2_small.gif", "icons/invader_3_small.gif"]
INVADER_ROWS = len(INVADER_ICONS_SMALL)
INVADER_SCORE = [30, 20, 10]
INVADERS_PER_ROW = 8

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_LINE_Y = -280
FINISH_LINE_Y = 280
BOTTOM_OF_SCOREBOARD_Y = 250
START_OF_ROAD = 300
END_OF_ROAD = -300
INVADER_GAP = 25
BALL_GAP = 50

class InvaderManager:
    def __init__(self, screen_dims, invader_icons_x):
        self.screen_dims = screen_dims
        self.invaders = {}    # Dictionary to hold invaders
        self.next_ord = 0
        self.invaders_per_row = INVADERS_PER_ROW
        self.add_start_gap = (self.screen_dims[0][1] - self.screen_dims[0][0] - self.invaders_per_row * (INVADER_WIDTH + INVADER_GAP) - INVADER_GAP) / 2
        self.end_gap = INVADER_GAP + self.add_start_gap
        i=0
        self.invader_icons = invader_icons_x
        self.add_invaders()

    def add_invaders(self):
        self.row_count = INVADER_ROWS
        # For each row and each column: add an invader
        for i in range(self.row_count):
            for j in range(self.invaders_per_row):
                self.invaders[self.next_ord] = Invader(i, j, self.end_gap, self.invader_icons[i])
                self.next_ord += 1

    def clear_invaders(self):
        for key in self.invaders:
            invader_x = self.invaders[key]
            invader_x.destroy_invader()
        self.invaders = {}
        self.next_ord = 0

    def move_invaders(self, direction):
        if direction == "Left":
            for key in self.invaders:
                invader_x = self.invaders[key]
                invader_x.move_left()
        elif direction == "Right":
            for key in self.invaders:
                invader_x = self.invaders[key]
                invader_x.move_right()
        else:
            pass

class Invader(Turtle):
    def __init__(self, invader_row, invader_column, end_gap_size, invader_icon):
        super().__init__()
        self.invader_icon = invader_icon
        self.left_edge = -250
        self.top_edge = 340
        self.invader_row = invader_row
        self.invader_column = invader_column
        self.end_gap_size = end_gap_size
        self.penup()
        self.build_invader()
        self.invader_score = INVADER_SCORE[self.invader_row]
        self.invader_left = 0
        self.position_invader(self.invader_row, self.invader_column)

    def destroy_invader(self):
        self.hideturtle()

    def Identify_Invader(self):
        self.color("black")

    def position_invader(self, row_pos, col_pos):
        x_coor = self.left_edge + self.end_gap_size + (self.shapesize()[1] * INITIAL_SHAPE_SIZE + INVADER_GAP) * col_pos + (
                    self.shapesize()[1] * INITIAL_SHAPE_SIZE / 2)
        y_coor = self.top_edge - (self.shapesize()[0] * INITIAL_SHAPE_SIZE + INVADER_GAP) * row_pos
        self.goto(x=x_coor, y=y_coor)
        self.set_location()

    def build_invader(self):
        self.shape(self.invader_icon)

    def set_location(self):
        """contains a nested list of the invader location left edge to right edge, bottom edge to top edge"""
        self.invader_left = self.xcor() - (self.shapesize()[1] * INITIAL_SHAPE_SIZE / 2)
        self.invader_right = self.xcor() + (self.shapesize()[1] * INITIAL_SHAPE_SIZE / 2)
        self.invader_bottom = self.ycor() - (self.shapesize()[0] * INITIAL_SHAPE_SIZE / 2)
        self.invader_top = self.ycor() + (self.shapesize()[0] * INITIAL_SHAPE_SIZE / 2)
        self.location = [(self.invader_left, self.invader_right), (self.invader_bottom, self.invader_top)]
        self.laser_turret_position = (self.xcor(), self.invader_bottom)

    def shoot_laser(self):
        return Laser(self.laser_turret_position, "Up")

    def move_left(self):
        if not self.invader_left - MOVE_INCREMENT < self.getscreen().window_width() / 2 * -1:
            self.goto(x=self.xcor() - MOVE_INCREMENT, y=self.ycor())
            self.set_location()

    def move_right(self):
        if not self.invader_right + MOVE_INCREMENT > self.getscreen().window_width() / 2:
            self.goto(x=self.xcor() + MOVE_INCREMENT, y=self.ycor())
            self.set_location()
