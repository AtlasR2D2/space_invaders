from invader_manager import InvaderManager
from laser import LaserManager
from spaceship import Spaceship
from scoreboard import PlayerLives, ScoreBoard
from intersect import Intersect
import random

MAX_INVADER_MOVE = 3


class SpaceInvadersGame:
    def __init__(self, initial_lives, screen_dims, invader_icons, spaceship_img):
        self.lives = initial_lives
        self.screen_dims = screen_dims
        self.invader_manager = InvaderManager(screen_dims=screen_dims, invader_icons_x=invader_icons)
        self.spaceship = Spaceship(spaceship_img=spaceship_img)
        self.laser_manager = LaserManager(screen_dims=screen_dims)
        self.score_board = ScoreBoard(screen_dims=screen_dims)
        self.lives_board = PlayerLives(screen_dims=screen_dims, initial_lives=self.lives)
        self.game_over = False
        self.space_invader_collective_pos = 0
        random.seed()
        self.space_invader_move_direction = random.choice(["Left", "Right"])

    def change_invader_move_direction(self):
        if self.space_invader_move_direction == "Left":
            return "Right"
        elif self.space_invader_move_direction == "Right":
            return "Left"

    def move_invaders(self):
        self.invader_manager.move_invaders(direction=self.space_invader_move_direction)
        if self.space_invader_move_direction == "Left":
            self.space_invader_collective_pos -= 1
        elif self.space_invader_move_direction == "Right":
            self.space_invader_collective_pos += 1

    def spaceship_shoot_laser(self):
        """shoots a laser point from the spaceship"""
        self.laser_manager.add_laser(starting_pos=self.spaceship.laser_turret_position, direction="Up")

    def invader_shoot_laser(self):
        """shoots a laser point from an invader"""
        eligible_invaders = []
        for col in range(self.invader_manager.invaders_per_row):
            max_row = -1
            blnInvaderFound = False
            invader_x = None
            for invader_key in self.invader_manager.invaders.keys():
                if self.invader_manager.invaders[invader_key].invader_column == col:
                    if self.invader_manager.invaders[invader_key].invader_row > max_row:
                        blnInvaderFound = True
                        max_row = self.invader_manager.invaders[invader_key].invader_row
                        invader_x = self.invader_manager.invaders[invader_key]
            if blnInvaderFound:
                eligible_invaders.append(invader_x)
        # Choose invader to shoot laser
        if len(eligible_invaders) != 0:
            # print(f"random_invader.: {len(eligible_invaders)}")
            random.seed()
            random_invader = random.choice(eligible_invaders)
            self.laser_manager.add_laser(starting_pos=random_invader.laser_turret_position, direction="Down")

    def reset_game(self):
        self.laser_manager.clear_lasers()
        self.spaceship.reset_game()

    def play_game(self):
        """move the laser point, check for collisions against edges and objects. Move the space invaders"""

        # Set equal to false incase there aren't any lasers yet
        blnCollision = False
        lasers_to_remove = []
        for laser_key in self.laser_manager.lasers:
            # Define laser_point
            laser_point = self.laser_manager.lasers[laser_key]
            blnCollision = False
            # Check if there are any invaders left | Increment level if all destroyed
            if len(self.invader_manager.invaders) == 0:
                self.invader_manager.add_invaders()
            # Check if collided with gutter | Remove laser point
            elif laser_point.location[1][0] <= self.screen_dims[1][0]:
                blnCollision = True
                laser_point.destroy_laser()  # Hide Laser Point
                lasers_to_remove.append(laser_key)  # Mark for removal
            # Check if collided with wall (Left/Right) | Remove laser point
            elif laser_point.location[0][0] - laser_point.move_increment < self.screen_dims[0][0] or laser_point.location[0][1] + laser_point.move_increment > self.screen_dims[0][1]:
                blnCollision = True
                laser_point.destroy_laser()  # Hide Laser Point
                lasers_to_remove.append(laser_key)  # Mark for removal
            # Check if collided with wall (Top) | Remove laser point
            elif laser_point.location[1][1] + laser_point.move_increment > self.screen_dims[1][1]:
                blnCollision = True
                laser_point.destroy_laser()  # Hide Laser Point
                lasers_to_remove.append(laser_key)  # Mark for removal
            # Check if collided with spaceship | Lose Life!
            elif Intersect(laser_point.location, self.spaceship.location) and laser_point.direction == "Down":
                blnCollision = True
                laser_point.destroy_laser()  # Hide Laser Point
                lasers_to_remove.append(laser_key)  # Mark for removal
                if self.lives_board.lives > 0:
                    # Continue playing, spaceship loses a life
                    self.lives_board.decrease_lives()
                    if self.lives_board.lives == 0:
                        self.game_over = True
                        break
                else:
                    # Exit loop
                    self.game_over = True
                    break
            # Check if collided with invader | Spaceship wins
            else:
                invaders_to_remove = []
                for invader_key in self.invader_manager.invaders:
                    invader_x = self.invader_manager.invaders[invader_key]
                    if Intersect(laser_point.location, invader_x.location) and laser_point.direction == "Up":
                        blnCollision = True
                        score_x = invader_x.invader_score
                        invader_x.destroy_invader()     # Hide Invader
                        invaders_to_remove.append(invader_key)    # Mark for removal
                        laser_point.destroy_laser()  # Hide Laser Point
                        lasers_to_remove.append(laser_key)  # Mark for removal
                        # Spaceship gets points
                        self.score_board.increment_score(score_inc=score_x)
                        break
                # Remove invader from invader manager
                for invader_key in invaders_to_remove:
                    self.invader_manager.invaders.pop(invader_key)
            # Otherwise just move the laser point
            if not blnCollision:
                laser_point.move()
        # Remove laser points from laser manager
        for laser_key in lasers_to_remove:
            self.laser_manager.lasers.pop(laser_key)

        return blnCollision
