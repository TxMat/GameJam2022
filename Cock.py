import pygame
from pygame.sprite import AbstractGroup


class Cock(pygame.sprite.Sprite):
    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
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

    def feed(self, gran_name):
        pass

    def add_perk(self, perk_name):
        pass

    def add_ritual(self, ritual_name):
        pass

    def lay_egg(self, new_name):
        pass

    def update(self, *args: Any, **kwargs: Any) -> None:
        pass

    def draw(self):
        pass