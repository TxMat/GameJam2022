import pygame.image


class Farm:
    def __init__(self):
        self.isNight = False
        self.HUD = None
        self.background_img = pygame.image.load("Assets/backgound_day.png")
        self.background = pygame.Surface((1024, 768))
        self.background.blit(self.background_img, (0, 0))

