import pygame
from pygame.sprite import AbstractGroup

MAX_MATURATION = 200
MAX_HUNGER = 100
STAT_INHERITANCE = 0.33

class Cock(pygame.sprite.Sprite):
    def __init__(self, *groups: AbstractGroup, id, name, intelligence = 1, strength = 1, stamina = 1, perks = set(), traits = set(), rituals = set(), fertile = True, maturation = 0, child = 0, parent = 0, hunger = MAX_HUNGER, tree = None, inheritance = STAT_INHERITANCE) -> None:
        super().__init__(*groups)
        self.index = 0
        self.id = id
        self.name = name
        self.intel = intelligence
        self.strength = strength
        self.stamina = stamina
        self.perks = perks
        self.traits = traits
        self.rituals = rituals
        self.fertile = fertile
        self.maturation = maturation
        self.child = child
        self.parent = parent
        self.hunger = hunger
        self.fed = {}
        self.tree = tree
        self.inheritance = inheritance

    def feed(self, grain_name, grain_dict, quantity) -> None:
        grain = grain_dict[grain_name]
        if grain_name not in self.fed.keys():
            self.fed[grain_name] = 0
        self.fed[grain_name] += quantity
        self.hunger += grain.hunger*quantity
        if self.hunger > MAX_HUNGER:
            self.hunger = MAX_HUNGER
        if self.maturation < MAX_MATURATION:
            self.intel += grain.int_bonus
            self.strength += grain.str_bonus
            self.stamina += grain.sta_bonus
        self.maturation

    def intel(self):
        intel = self.intel
        for rit in self.rituals:
            ritual = ritual_dict[rit]
            intel *= ritual.int_mult
            intel += ritual.int_mod
        for perks in self.perks:
            perk = perk_dict[perks]
            intel *= perk.int_mult
            intek += perk.int_mod
        return intel
            
    def strength(self):
        strength = self.strength
        for rit in self.rituals:
            ritual = ritual_dict[rit]
            strength *= ritual.str_mult
            strength += ritual.str_mod
        for perks in self.perks:
            perk = perk_dict[perks]
            strength *= perk.str_mult
            strength += perk.str_mod
        return strength

    def stamina(self):
        stam = self.intel
        for rit in self.rituals:
            ritual = ritual_dict[rit]
            stam *= ritual.sta_mult
            stam += ritual.sta_mod
        for perks in self.perks:
            perk = perk_dict[perks]
            stam *= perk.sta_mult
            stam += perk.sta_mod
        return stam

    def add_perk(self, perk_name) -> None:
        self.perks.add(perk_name)
        perk_dict[perk_bame].action(self)

    def add_ritual(self, ritual_name) -> None:
        self.rituals.add(ritual_name)
        ritual_dict[ritual_name].action(self)

    def lay_egg(self, new_name, new_id): -> Cock
        if(self.fertile == True):
            return Cock(id,
                        name,
                        self.intel()*self.inheritance,
                        self.strength()*self.inheritance,
                        self.stamina()*self.inheritance)
            self.fertile = False

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
