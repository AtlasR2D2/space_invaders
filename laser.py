from turtle import Turtle
import random
import time

INITIAL_BALL_SIZE = 20
BALL_WIDTH = 10
BALL_HEIGHT = 5
INITIAL_POS_X = 0
# INITIAL_POS_Y = 0
MOVE_INCREMENT = 2
SLEEP_AMOUNT = 0.00002

class LaserManager:
        def __init__(self, screen_dims):
            self.screen_dims = screen_dims
            self.lasers = {}  # Dictionary to hold laser points
            self.next_ord = 0

        def add_laser(self, starting_pos, direction):
            """add a laser point to the laser manager"""
            self.lasers[self.next_ord] = Laser(starting_pos=starting_pos, direction=direction)
            self.next_ord += 1

        def clear_lasers(self):
            for key in self.lasers:
                laser_x = self.lasers[key]
                laser_x.destroy_laser()
            self.lasers = {}
            self.next_ord = 0

        def move_lasers(self):
            """move all laser points one move increment"""
            for key in self.lasers:
                laser_x = self.lasers[key]
                laser_x.move()

class Laser(Turtle):
    def __init__(self, starting_pos, direction):
        super().__init__()
        self.starting_pos = starting_pos
        self.direction = direction
        self.move_increment = MOVE_INCREMENT
        self.shape("square")
        self.shapesize(stretch_wid=BALL_HEIGHT/INITIAL_BALL_SIZE, stretch_len=BALL_WIDTH/INITIAL_BALL_SIZE)
        self.fillcolor("white")
        self.penup()
        self.initialise_laser()
        self.new_heading = self.heading()
        self.speed("fastest")

    def change_direction(self):
        if self.direction == "Up":
            self.direction = "Down"
        elif self.direction == "Down":
            self.direction = "Up"

    def initialise_laser(self):
        self.goto(x=self.starting_pos[0], y=self.starting_pos[1])
        self.set_laser_ends()
        # Set direction of laser travel
        if self.direction == "Up":
            self.new_heading = 90
        else:
            # Down
            self.new_heading = 270
        self.setheading(self.new_heading)

    def set_laser_ends(self):
        self.laser_top_y = self.ycor() + self.shapesize()[0] * INITIAL_BALL_SIZE / 2
        self.laser_bottom_y = self.ycor() - self.shapesize()[0] * INITIAL_BALL_SIZE / 2
        self.laser_left_x = self.xcor() - self.shapesize()[0] * INITIAL_BALL_SIZE / 2
        self.laser_right_x = self.xcor() + self.shapesize()[0] * INITIAL_BALL_SIZE / 2
        self.laser_left_y = self.ycor()
        self.laser_right_y = self.ycor()
        self.location = [(self.laser_left_x, self.laser_right_x), (self.laser_bottom_y, self.laser_top_y)]

    def move(self):
        """function will move the ball if it doesn't hit a wall"""
        """returns true if was able to move, false otherwise"""
        #time.sleep(SLEEP_AMOUNT)  # Use if you want to slow it down
        self.forward(MOVE_INCREMENT)
        self.set_laser_ends()
        return True

    def destroy_laser(self):
        self.hideturtle()