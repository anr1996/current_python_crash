
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.screen = pygame.display.set_mode((1200, 800))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
                  
          
    def _check_events(self):
            """Respond to keypresses and mouse events."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    
                    
    def _check_keydown_events(self, event):
        
        if event.key == pygame.K_q:
            sys.exit()
        
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
                    
            
    def _check_keyup_events(self, event): 
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
                    
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
                                    
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
        
            
    def _update_bullets(self):
        """Update the position of bullets and get rid of old bullets."""
        # Update bullets positions.
        self.bullets.update()
        
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)              
        
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
            
    
if __name__ == '__main__':
    # Make a game instance, and run the game.
        
    ai = AlienInvasion()
    ai.run_game()

