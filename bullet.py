import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Initialize the bullet and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.colour = self.settings.bullet_color

    #--------------CREATE A BULLET RECT AT (0,0) THEN SET CORRECT POSITION------------
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the bullet's position as a float
        self.y = float(self.rect.y)


    def update(self):
        """Update the bullet position"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y


    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)

