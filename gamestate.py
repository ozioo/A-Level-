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

font = "NbpReadout-RBVA.ttf"

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE=(0,0,255)
RED = (255, 0, 0)
(x,y) = (800,800)   
deg = 0            
enemy_count= 0 
game_end= False
pygame.init()       
pygame.display.set_mode((1000, 1000), 0, 32) 
screen = pygame.display.get_surface()
pygame.init()

score= 0

all_sprites_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
class Cursor(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    def __init__(self, image,x ,y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([40, 40])
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(center = (x, y))
        self.image=image
    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, x_pos, y_pos,x_d,y_d):
        super().__init__()
        # Set height, width
        self.image = pygame.Surface([20, 20])
        self.image= image
        self.mask = pygame.mask.from_surface(self.image)
        self.y_d = y_d
        self.x_d = x_d
        self.lock_time = 0
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y_pos
        self.rect.x = x_pos

    def change_state(self, image):
        #print ('test')
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.x_d
        self.rect.y += self.y_d

class Friendly(Enemy):
    pass
    
class Base(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

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

        dx = x/2 + x/2 * math.cos(math.radians(self.angle-.1))
        dy = y/2 + x/2 * math.sin(math.radians(self.angle-.1))
        f = .1
        self.image.fill(0)
        pygame.draw.aaline(self.image, (0, int(255/(1+f)), 0), (int(x/2), int(y/2)), (dx, dy),5)
        self.mask = pygame.mask.from_surface(self.image)
def MAP():
    
    pygame.draw.circle(screen, (102, 255, 102), (int(x/2), int(y/2)), int(x/2), 1)
    pygame.draw.circle(screen, (102, 255, 102), (int(x/2), int(y/2)), int(x/4), 1)
    pygame.draw.line(screen, (76, 82, 76), (250, 190), (200, 55))
    pygame.draw.line(screen, (76, 82, 76), (300, 200), (250, 190))
    pygame.draw.line(screen, (76, 82, 76), (350, 300), (300, 200))
    pygame.draw.line(screen, (76, 82, 76), (350, 300), (785, 300))
    pygame.draw.line(screen, (76, 82, 76), (340, 360), (0, 400))
    pygame.draw.line(screen, (76, 82, 76), (350, 300), (300, 600))
    pygame.draw.line(screen, (76, 82, 76), (300, 600), (350, 675))
    pygame.draw.line(screen, (76, 82, 76), (370, 796), (350, 675))

def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText



def main_menu():
 
    menu=True
    controls=False
    selected="start"
 
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_RIGHT:
                    selected="quit"
                elif event.key==pygame.K_LEFT:
                    selected="Controls"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        menu = False
                    if selected=="Controls":
                        menu = False
                        controls=True
                    if selected=="quit":
                        pygame.quit()
                        quit()
 
        # Main Menu UI
        screen.fill(BLACK)
        title=text_format("Missile Command Redux", font, 50, GREEN)
        if selected=="start":
            text_start=text_format("START", font, 40, WHITE)
        else:
            text_start = text_format("START", font, 40, GREEN)
        if selected=="Controls":
            text_controls=text_format("CONTROLS", font, 40, WHITE)
        else:
            text_controls = text_format("CONTROLS", font, 40, GREEN)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 40, WHITE)
        else:
            text_quit = text_format("QUIT", font, 40, GREEN)
 
        text_tutorial1= text_format("USE THE MOUSE BUTTON TO MOVE THE CURSOR", font, 23, GREEN)
        text_tutorial2= text_format("BRING THE CURSOR ONTOP OF THE ENEMIES, THE GREEN BLIPS", font, 23, GREEN)
        text_tutorial3= text_format("PRESS THE ENTER KEY TO LOCK THEM", font, 23, GREEN)
        text_tutorial4= text_format("WHEN LOCKED PRESS SPACEBAR TO SHOOT THEM DOWN", font, 23, GREEN)
        text_tutorial5= text_format("IF THE ENEMIES REACH YOUR BASE IT IS GAME OVER", font, 23, GREEN)
        text_tutorial6= text_format("DO NOT SHOOT THE FRIENDLIES", font, 23, BLUE)
        
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(title, (1000/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (1000/2 - (start_rect[2]/2), 300))
        screen.blit(text_controls, (600/2 - (start_rect[2]/2), 360))
        screen.blit(text_quit, (1250/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(60) 
    
    while controls:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="back"
                if event.key==pygame.K_RETURN:
                    if selected=="back":
                        main_menu()
                        


        # Main Menu UI
        screen.fill(BLACK)
        
        title=text_format("Controls", font, 50, GREEN)
        text_quit = text_format("USE THE MOUSE BUTTON TO MOVE THE CURSOR", font, 20, GREEN)

        



       

 
        # Main Menu Text
        screen.blit(title, (1000/2 - (title_rect[2]/2), 160))
        
        #screen.blit(title2 , (1000/2 - (title2[2]/2), 80))
        screen.blit(text_tutorial1, (1000/2 - (480), 300))
        screen.blit(text_tutorial2, (1000/2 - (480), 360))
        screen.blit(text_tutorial3, (1000/2 - (480), 420))
        screen.blit(text_tutorial4, (1000/2 - (480), 480))
        screen.blit(text_tutorial5, (1000/2 - (480), 540))
        screen.blit(text_tutorial6, (1000/2 - (480), 600))
        pygame.display.update()
        clock.tick(60)

def Enemy_Spawn(number):
    locations=[]
    global enemy_count
    locations = random.sample(range(8),number)
    for i in range(number):
        if locations[i]==1:
            enemy=Enemy(UNLOCK,400,100,0,1)
            all_sprites_list.add(enemy)
            enemy_list.add(enemy)
            enemy_count =+ 1
        elif locations[i] == 2:
            enemy=Enemy(UNLOCK,150,100,1,1)
            all_sprites_list.add(enemy)
            enemy_list.add(enemy)
            enemy_count =+ 1
        elif locations[i] == 3:
            enemy=Enemy(UNLOCK,100,400,1,0)
            all_sprites_list.add(enemy)
            enemy_list.add(enemy)
            enemy_count =+ 1
        elif locations[i] == 4:
            enemy=Enemy(UNLOCK,150,600,1,-1)
            all_sprites_list.add(enemy)
            enemy_list.add(enemy)
            enemy_count =+ 1
        elif locations[i] == 5:
            enemy=Enemy(UNLOCK,400,700,0,-1)
            all_sprites_list.add(enemy)
            enemy_list.add(enemy)
            enemy_count =+ 1
        elif locations[i] == 6:
            enemy=Enemy(UNLOCK,600,600,-1,-1)
            all_sprites_list.add(enemy)
            enemy_count =+ 1
            enemy_list.add(enemy)
        elif locations[i] == 7:
            enemy=Enemy(UNLOCK,700,400,-1,0)
            all_sprites_list.add(enemy)
            enemy_list.add(enemy)
            enemy_count =+ 1
        elif locations[i] == 8:
            enemy=Enemy(UNLOCK,650,150,-1,1)
            all_sprites_list.add(enemy)
            enemy_list.add(enemy)
            enemy_count =+ 1
    locations=[]
          
current_time=0
# Set the width and height of the screen [width, height]

#def radar_detection

#def lock
pygame.display.set_caption("Missile Command Redux")
# Loop until the user clicks the close button.


done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


radar =Line(400,400)
cursor =Cursor(CURSOR,372,375)

Enemy_Spawn(5)

all_sprites_list.add(radar)
all_sprites_list.add(cursor)

# -------- Main Program Loop -----------
##black=(0,0,0)
##end_it=False
##while (end_it==False):
##    screen.fill(black)
##    myfont=pygame.font.SysFont("NBP Readout", 40)
#    nlabel=myfont.render("Welcome ", 1, (255, 0, 0))
#    for event in pygame.event.get():
#        if event.type==MOUSEBUTTONDOWN:
#            end_it=True
#    screen.blit(nlabel,(200,200))
#    pygame.display.flip()
main_menu()


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
 
    # --- Game logic should go here
    #MAP()
    if game_end == False:
        pygame.draw.circle(screen, (102, 255, 102), (int(x/2), int(y/2)), int(x/2), 1)
        pygame.draw.circle(screen, (102, 255, 102), (int(x/2), int(y/2)), int(x/4), 1)
        pygame.draw.line(screen, (76, 82, 76), (250, 190), (200, 55))
        pygame.draw.line(screen, (76, 82, 76), (300, 200), (250, 190))
        pygame.draw.line(screen, (76, 82, 76), (350, 300), (300, 200))
        pygame.draw.line(screen, (76, 82, 76), (350, 300), (785, 300))
        pygame.draw.line(screen, (76, 82, 76), (340, 360), (0, 400))
        pygame.draw.line(screen, (76, 82, 76), (350, 300), (300, 600))
        pygame.draw.line(screen, (76, 82, 76), (300, 600), (350, 675))
        pygame.draw.line(screen, (76, 82, 76), (370, 796), (350, 675))

    current_time= pygame.time.get_ticks()
        #pygame.draw.line(screen, (0, 200, 0), (int(x/2), 0), (int(x/2), y))
    #for enemy in enemy_list:

        #if pygame.sprite.collide_mask(enemy,radar):
            #enemy.change_state(LOCK)
            #enemy.lock_time = pygame.time.get_ticks()
    
    #for enemy in enemy_list:
        #if pygame.spritecollide_mask(enemy,radar):
            
        
        


    for e in enemy_list:
        if pygame.sprite.collide_mask(e, radar):
            e.change_state(LOCK)
            score =+ 10
            #game_end = True 

    

    all_sprites_list.update()
    pygame.display.update()     
    clock.tick(60)        
    screen.fill((0, 0, 0, 0))


    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    all_sprites_list.draw(screen)
    if game_end == True:
        screen.fill((102, 255, 102, 0))
    # If you want a background image, replace this clear with blit'ing the
    # background image.

 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
 
    # --- Limit to 60 frames per second

 
# Close the window and quit.
pygame.quit()
