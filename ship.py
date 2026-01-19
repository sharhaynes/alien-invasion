import pygame

class Ship:
    def __init__ (self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and get its rect
        self.image = pygame.image.load('Images/ship001.png')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom centre of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)

        #-------MOVEMENT FLAG: START WITH A NON-MOVING SHIP-------
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        #update teh ship's x value and not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #UPDATE TEH RECT OBJECT FROM SELF X
        self.rect.x = self.x

    def centre_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)