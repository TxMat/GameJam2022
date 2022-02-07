import pygame

# init lib
pygame.init()

# create screen
screen = pygame.display.set_mode((1024, 768))



# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False