import os
import random
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

UNLOCK = pygame.image.load('pixilart-drawing.png')

LOCK = pygame.image.load('pixil-frame-0.png')

CURSOR = pygame.image.load('pixil-frame-0 (1).png')

INVIS = pygame.image.load('pixil-frame-0 (2).png')

class enemy(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    def __init__(self, image):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([40, 40])
        
        self.image=image

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = 100
        self.rect.x = 70
    def change_state(self, image):
        self.image = image

class cursor(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    def __init__(self, image,x ,y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([60, 60])
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.change_x = 0
        self.change_y = 0
        self.image=image

        # Make our top-left corner the passed-in location.




        





pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("press enter to lock the target")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
all_sprites_list = pygame.sprite.Group()
enemy = enemy(UNLOCK)
cursor = cursor(CURSOR,340,240)
all_sprites_list.add(enemy)
all_sprites_list.add(cursor)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cursor.rect.x -= 10 
            elif event.key == pygame.K_RIGHT:
                cursor.rect.x += 10

            elif event.key == pygame.K_UP:
                cursor.rect.y -= 10

            elif event.key == pygame.K_DOWN:
                cursor.rect.y += 20
            elif event.key == pygame.K_RETURN:
                if pygame.sprite.collide_rect(cursor,enemy) == True:
                    enemy.change_state(LOCK)
                else:
                    enemy.change_state(UNLOCK)

                

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
