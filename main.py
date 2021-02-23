import turtle
from turtle import Screen, Turtle
from space_invaders_game import SpaceInvadersGame, MAX_INVADER_MOVE
from invader_manager import InvaderManager, INVADER_ICONS_SMALL
from spaceship import SPACESHIP_IMG, Spaceship
from laser import Laser
from random import choice

screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=900)
screen.title("Space Invaders")

screen.tracer(0)

# Screen Dimension Variables
SCREEN_TOP = screen.window_height() / 2
SCREEN_BOTTOM = screen.window_height() / 2 * -1
SCREEN_LEFT = screen.window_width() / 2 * -1
SCREEN_RIGHT = screen.window_width() / 2
SCREEN_DIMS = [(SCREEN_LEFT, SCREEN_RIGHT), (SCREEN_BOTTOM, SCREEN_TOP)]

# Load invader_icons
invader_icons = []
i = 0
for icon in INVADER_ICONS_SMALL:
    invader_icons.append(icon)
    screen.addshape(invader_icons[i])
    i += 1
screen.addshape(SPACESHIP_IMG)

# Initialise Game
space_invaders_game = SpaceInvadersGame(initial_lives=3,screen_dims=SCREEN_DIMS,invader_icons=invader_icons, spaceship_img=SPACESHIP_IMG)

#
# # The game is watching your moves
screen.listen()
screen.onkey(fun=space_invaders_game.spaceship.move_left, key="Left")
screen.onkey(fun=space_invaders_game.spaceship.move_right, key="Right")
screen.onkey(fun=space_invaders_game.spaceship_shoot_laser, key="space")

game_is_on = True
loop_counter = 0

invader_shoot_rand_time_inc = [40, 30, 50, 55]

while game_is_on:
    # Update the screen
    screen.update()
    # Move the ball
    space_invaders_game.play_game()
    # Check if game is over
    if space_invaders_game.game_over:
        space_invaders_game.lives_board.game_over()
        game_is_on = False
    else:
        # Move the space invaders
        if loop_counter % 25 == 0:
            if abs(space_invaders_game.space_invader_collective_pos) == MAX_INVADER_MOVE:
                space_invaders_game.space_invader_move_direction = space_invaders_game.change_invader_move_direction()
            space_invaders_game.move_invaders()
        elif loop_counter % choice(invader_shoot_rand_time_inc) == 0:
            space_invaders_game.invader_shoot_laser()
    loop_counter += 1

screen.exitonclick()
