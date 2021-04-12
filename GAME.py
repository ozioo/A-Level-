import math
import pygame

UNLOCK = pygame.image.load('pixilart-drawing.png')

LOCK = pygame.image.load('pixil-frame-0.png')

CURSOR = pygame.image.load('pixil-frame-0 (1).png')

INVIS = pygame.image.load('pixil-frame-0 (2).png')

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center = (x, y))
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
    def change_state(self, image):
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)

class Line(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((200, 200))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center = (x, y))
        self.angle = 0
    def update(self):
        vec = round(math.cos(self.angle * math.pi / 180) * 100), round(math.sin(self.angle * math.pi / 180) * 100)
        self.angle = (self.angle + 3) % 360
        self.image.fill(0)
        pygame.draw.line(self.image, (255, 255, 0), (100 - vec[0], 100 - vec[1]), (100 + vec[0], 100 + vec[1]), 5)
        self.mask = pygame.mask.from_surface(self.image)
        
pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

sprite_image = LOCK.convert_alpha()
moving_object = SpriteObject(0, 0, sprite_image)
line_object = Line(*window.get_rect().center)
all_sprites = pygame.sprite.Group([moving_object, line_object])
red = 0

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
 
    all_sprites.update()

    if pygame.sprite.collide_mask(moving_object, line_object):
        moving_object.change_state(pygame.image.load('pixilart-drawing.png'))

    window.fill((0, 0, 0))
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit()