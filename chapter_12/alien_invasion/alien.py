import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen 
        
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('/Users/adrianrich/Documents'
                                       '/python_crash_course_current/chapter_12'
                                       '/alien_invasion/images/green_alien.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (80, 80)) 
        
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width / 12
        self.rect.y = self.rect.height / 22
        
        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        
        