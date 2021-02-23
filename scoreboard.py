from turtle import Turtle

FONT = {"Arial", 16, "Bold"}
ALIGNMENT = "Center"

class ScoreBoard(Turtle):
    def __init__(self, screen_dims):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        x_coord = (screen_dims[0][1] - screen_dims[0][0]) / 4 * -1
        y_coord = (screen_dims[1][1] - screen_dims[1][0]) * 2 / 5
        self.goto(x_coord, y_coord)
        self.score = 0
        self.show_score()

    def increment_score(self, score_inc):
        self.score += score_inc
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(arg=f"SCORE {self.score}", align=ALIGNMENT, font=FONT)


class PlayerLives(Turtle):
    def __init__(self, initial_lives, screen_dims):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        x_coord = (screen_dims[0][1] - screen_dims[0][0]) / 4
        y_coord = (screen_dims[1][1] - screen_dims[1][0]) * 2/5
        self.goto(x_coord, y_coord)
        self.lives = initial_lives
        self.show_lives()

    def decrease_lives(self):
        self.lives -= 1
        self.show_lives()

    def show_lives(self):
        self.clear()
        self.write(arg=f"LIVES {self.lives}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"GAME OVER.\nNO MORE LIVES REMAINING.", align=ALIGNMENT, font=FONT)