import pygame
import Utils
import time
# init lib
pygame.init()
clock = pygame.time.Clock()
# create screen
HEIGHT = 1024
WIDTH = 768
screen = pygame.display.set_mode((HEIGHT, WIDTH))

screen.fill((0,0,0))
clock.tick(60)

img = Utils.frames_from_spritesheet("Assets/cock_walk.png", 0, 0, 48, 48, 6)

curr_img = 0

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    finalrdr = pygame.transform.scale(img[curr_img%len(img)], (48*5,48*5))
    screen.blit(pygame.transform.flip(finalrdr, False, False), (200, 200))
    pygame.display.update()
    curr_img += 1
    time.sleep(0.17)
