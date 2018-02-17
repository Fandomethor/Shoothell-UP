import pygame
import random
##
from const import *
from settings import *
from player import *

# Initialize pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shoothell UP")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
#Game loop
loop = True
while loop:
    clock.tick(FPS)

    #Update
    all_sprites.update()

    #Draw
    screen.fill(BLUE)
    all_sprites.draw(screen)

    pygame.display.flip()

    # Check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.K_ESCAPE in pygame.key.get_pressed():
            loop = False

pygame.quit()
