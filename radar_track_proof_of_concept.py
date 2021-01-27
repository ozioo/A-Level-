"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class enemy(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    def __init__(self, color):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([40, 40])
        self.image.fill(color)
        self.color=color
        self.move=1
        self.move_y=1
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
    def change_color(self, color):
        self.color = color
        self.image.fill(self.color)
    def update(self):
        

        self.rect.x += self.move_y



pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("press left arrow for it to lose track")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
all_sprites_list = pygame.sprite.Group()
enemy = enemy((0,255,0))
all_sprites_list.add(enemy)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if enemy.color == (0,255,0):
                    enemy.change_color((0,0,0))
                elif enemy.color == (0,0,0):
                    enemy.change_color((0,255,0))
    # --- Game logic should go here
    all_sprites_list.update()
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    
    # --- Drawing code should go here
    all_sprites_list.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()