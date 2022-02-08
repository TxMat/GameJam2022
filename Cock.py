import pygame
from pygame.sprite import AbstractGroup


class Cock(pygame.sprite.Sprite):
    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        self.index = 0
        self.id = 0
        self.name = ""
        self.intelligence = 0
        self.strength = 0
        self.stamina = 0
        self.perks = []
        self.traits = []
        self.rituals = []
        self.fertile = True
        self.maturation = 0
        self.child = 0
        self.parent = 0
        self.hunger = 100

    def feed(self, grain_name):
        pass

    def add_perk(self, perk_name):
        pass

    def add_ritual(self, ritual_name):
        pass

    def lay_egg(self, new_name):
        pass

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

        # img = Utils.frames_from_spritesheet("Assets/cock_walk.png", 0, 0, 48, 48, 6)
        ## anim ##
        # curr_img = 0
        #     finalrdr = pygame.transform.scale(img[curr_img%len(img)], (48*5,48*5))
        #     screen.blit(pygame.transform.flip(finalrdr, False, False), (200, 200))
        #     pygame.display.update()
        #     curr_img += 1
        #     time.sleep(0.17)

    def draw(self):
        pass
