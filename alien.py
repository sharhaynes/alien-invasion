import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien"""
    def __init__(self, ai_game):
        """Initialize alien's attributes"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the alien image and set its rect attribute
        self.image = pygame.image.load('Images/alien.bmp')
        self.rect = self.image.get_rect()

        #sstart each new alien near the top left od the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Check if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Update the alien's position"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x


