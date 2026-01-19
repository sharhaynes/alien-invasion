#------------IMPORTATIONS-----------
import sys
from time import sleep
import pygame

#---------MAKE INSTANCES OF DIFFERENT FILES-------------
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
#-----------CREATE ALIEN INVASION CLASS-------------------
class AlienInvasion:
    """ Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialise the game and create the game resources"""
        pygame.init() #always have to initialise pygame

        self.clock = pygame.time.Clock()
        self.settings = Settings()

#-------------------GETTING FULL SCREEN MODE-----------------------------
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

#---------------------SCREEN SETTINGS----------------------------
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.create_fleet()
        self.game_active = True


#---------------GAME LOOP--------------
    def check_events(self):
        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown(event)

    #-----------------KEY UP TO STOP MOVING-----------------------
            elif event.type == pygame.KEYUP:
                self.check_keyup(event)


    def check_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_bullets(self):
        """UPDATE POSITION OF BULLETS AND GET RID OF OLD BULLETS"""
        self.bullets.update()

        # get rid of bullets that disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self.check_bullet_alien_collisions()

    def check_bullet_alien_collisions(self):
        #USING THIS TO RESPODN TO THE COLLISIONS BETWEEN THE ALIEN AND THE BULLET
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            #destroy all of the existing bullets and create new fleet
            self.bullets.empty()
            self.create_fleet()

    def create_fleet(self):
        """Create the fleet of aliens"""
        alien = Alien(self)

#---------------SPACING BETWEEN ALIENS IS ONE ALIEN WIDTH AND ONE ALIEN HEIGHT-------------------
        alien_width, alien_height = alien.rect.size

        current_x_position, current_y_position = alien_width, alien_height
        while current_y_position < (self.settings.screen_height - 3 * alien_height):
            while current_x_position < (self.settings.screen_width - 2 * alien_width):
                self.create_alien(current_x_position, current_y_position)
                current_x_position += 2 * alien_width

            #finished a row; reset x value and increment y value
            current_x_position = alien_width
            current_y_position += 2 * alien_height

        self.aliens.add(alien)

    def create_alien(self, x_position, y_position):
        """Create the alien and put it in the fleet"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.y = y_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)

    def update_aliens(self):
        """Update the aliens and their positions within the fleet"""
        self.check_fleet_edges()
        self.aliens.update()

        #look for any collisiosn between the alien and the ships
        if pygame.sprite.spritecollide(self.ship, self.aliens, True):
            self.ship_hit()

        #look for aliens hitting screen bottom
        self.check_aliens_bottom()

    def ship_hit(self):
        if self.stats.ships_left > 0:

        #decrement the amt of ships remaining
            self.stats.ships_left -=1

            self.bullets.empty()
            self.aliens.empty()

            self.create_fleet()
            self.ship.centre_ship()

            sleep(0.5)
        else:
            self.game_active = False


    def check_aliens_bottom(self):
        """CHECK IS THE ALIENS REACH BOTTOM OF SCREEN"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self.ship_hit()
                break

    def check_fleet_edges(self):
        """Respond approporaitely if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


#------------------------------UPDATE SCREEN--------------------------------------
    def update_screen(self):
        # redraw the screen durin each pass through the loop
        self.screen.fill(self.settings.bg_colour)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # draw the screen and make it visible
        pygame.display.flip()

    def run_game(self):
        """start main loop for the game"""
        while True:
            self.check_events()

            if self.game_active:

                self.ship.update()
                self.update_bullets()
                self.update_aliens()

            self.update_screen()
            self.clock.tick(60)


if __name__ == '__main__':
 # Make a game instance, and run the game.
 ai = AlienInvasion()
 ai.run_game()


