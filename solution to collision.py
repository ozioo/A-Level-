import sys
import pygame
import math
import random
from time import sleep
from pygame.locals import *


UNLOCK = pygame.image.load('UNLOCK.png')

LOCK = pygame.image.load('LOCK.png')

CURSOR = pygame.image.load('CURSOR.png')

INVIS = pygame.image.load('INVIS.png')
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
(x,y) = (800,800)   
deg = 0            
enemy_count= 0 
pygame.init()       
pygame.display.set_mode((1000, 1000), 0, 32) 
screen = pygame.display.get_surface()
pygame.init()

all_sprites_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center = (x, y))
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Line(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((800, 800))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center = (400, 400))
        self.angle = 0
    def update(self):
        self.angle +=1
        if self.angle >=360:
            deg=0
        i =1
        dx = x/2 + x/2 * math.cos(math.radians(self.angle-.1*i))
        dy = y/2 + x/2 * math.sin(math.radians(self.angle-.1*i))
        f = 1*.1
        self.image.fill(0)
        pygame.draw.aaline(self.image, (0, int(255/(1+f)), 0), (int(x/2), int(y/2)), (dx, dy),5)
        self.mask = pygame.mask.from_surface(self.image)



pygame.display.set_caption("Missile Command Redux")
# Loop until the user clicks the close button.


done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

moving_object = SpriteObject(0, 0, CURSOR)
all_sprites_list.add(moving_object)
radar =Line(400,400)

all_sprites_list.add(radar)

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

    if pygame.sprite.collide_mask(moving_object, radar):
        exit()
    else: 
        red = 0

    all_sprites_list.update()
    pygame.display.update()
     
    clock.tick(60)        
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


