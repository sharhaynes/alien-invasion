#--------------USE THIS FOR ALL OF THE SETTINGS WITHIN ALIEN INVASION-------
import pygame


class Settings:
    def __init__(self):
        #screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_colour = (230, 230, 230)

        #ship settings
        self.ship_speed = 5
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 6
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #alien settings
        self.alien_speed = 3
        self.fleet_drop_speed = 10
        #fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1