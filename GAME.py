import sys
import pygame
import math
from pygame.locals import *


UNLOCK = pygame.image.load('pixilart-drawing.png')

LOCK = pygame.image.load('pixil-frame-0.png')

CURSOR = pygame.image.load('pixil-frame-0 (1).png')

INVIS = pygame.image.load('pixil-frame-0 (2).png')
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
(x,y) = (800,800)   
deg = 0             
pygame.init()       
pygame.display.set_mode((1000, 1000), 0, 32) 
screen = pygame.display.get_surface()
pygame.init()

#class Cursor(pygame.sprite.Sprite):
#   def __init__(self,  x, y):
#
#    def update(self):
#
class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, x_pos, y_pos):
        super().__init__()
        # Set height, width
        self.image = pygame.Surface([40, 40])
        self.image= image
        self.mask = pygame.mask.from_surface(self.image)
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y_pos
        self.rect.x = x_pos
    def change_state(self, image):
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
    #def update(self):


    


class Line(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((800, 800))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center = (400, 400))
        self.angle = 0
    def update(self):
        self.angle +=4
        if self.angle >=360:
            deg=0
        for i in range(1, 10):
            dx = x/2 + x/2 * math.cos(math.radians(self.angle-.1*i))
            dy = y/2 + x/2 * math.sin(math.radians(self.angle-.1*i))
            f = i*.1
            pygame.draw.aaline(screen, (0, int(255/(1+f)), 0), (int(x/2), int(y/2)), (dx, dy),5)
        self.mask = pygame.mask.from_surface(self.image)
 
# Set the width and height of the screen [width, height]

#def radar_detection

#def lock
pygame.display.set_caption("Missile Command Redux")
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()
radar =Line(400,400)
enemy = Enemy(UNLOCK,200,200)
all_sprites_list.add(radar)
all_sprites_list.add(enemy)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    deg += 2
    if deg >= 360:  
        deg = 0

    pygame.draw.circle(screen, (102, 255, 102), (int(x/2), int(y/2)), int(x/2), 1)
    pygame.draw.circle(screen, (102, 255, 102), (int(x/2), int(y/2)), int(x/4), 1)
    pygame.draw.line(screen, (76, 82, 76), (250, 190), (200, 55))
    pygame.draw.line(screen, (76, 82, 76), (300, 200), (250, 190))
    pygame.draw.line(screen, (76, 82, 76), (350, 300), (300, 200))
    pygame.draw.line(screen, (76, 82, 76), (350, 300), (785, 300))
    pygame.draw.line(screen, (76, 82, 76), (350, 300), (300, 600))
    pygame.draw.line(screen, (76, 82, 76), (300, 600), (350, 675))
    pygame.draw.line(screen, (76, 82, 76), (370, 796), (350, 675))

        #pygame.draw.line(screen, (0, 200, 0), (int(x/2), 0), (int(x/2), y))


    all_sprites_list.update()
    pygame.display.update()     
    clock.tick(30)        
    screen.fill((0, 0, 0, 0))    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    all_sprites_list.draw(screen)
    # If you want a background image, replace this clear with blit'ing the
    # background image.

 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second

 
# Close the window and quit.
pygame.quit()
