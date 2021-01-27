# -*- coding: utf-8 -*-
import sys
import pygame
import math
from pygame.locals import *



def main():
    (x,y) = (800,800)   
    deg = 0             
    pygame.init()       
    pygame.display.set_mode((1000, 1000), 0, 32) 
    screen = pygame.display.get_surface()

    while (1):
        
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

        for i in range(1, 10):
            dx = x/2 + x/2 * math.cos(math.radians(deg-.1*i))
            dy = y/2 + x/2 * math.sin(math.radians(deg-.1*i))
            f = i*.1
            pygame.draw.aaline(screen, (0, int(255/(1+f)), 0), (int(x/2), int(y/2)), (dx, dy),5)

        pygame.display.update()     
        pygame.time.wait(30)        
        screen.fill((0, 0, 0, 0))  

        
        for event in pygame.event.get():
            if event.type == QUIT:      
                pygame.quit()           
                sys.exit()


if __name__ == "__main__":
        main()