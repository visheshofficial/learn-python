import sys

import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assests and behaviour."""
    
    def __init__(self) -> None:
        "Initializing game and create game resources."
        self.settings = Settings()
        pygame.init()
        self.screen =pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock=pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion")
        self.ship=Ship(self)
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        """Responses to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()   
                    