import pygame
from pygame.sprite import AbstractGroup

MAX_MATURATION = 200
MAX_HUNGER = 100
STAT_INHERITANCE = 0.33

class Cock(pygame.sprite.Sprite):
    def __init__(self,
                id,
                name,
                intelligence = 1,
                strength = 1,
                stamina = 1,
                perks = set(),
                traits = set(),
                rituals = set(),
                fertile = True,
                maturation = 0,
                child = 0,
                parent = 0,
                hunger = MAX_HUNGER,
                tree = None,
                inheritance = STAT_INHERITANCE,
                *groups: AbstractGroup) -> None:
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

    def info_cock(self):
        print("index: " + str(self.index))
        print("id: " + str(self.id))
        print("name: " + str(self.name))
        print("int: " + str(self.intel))
        print("str: " + str(self.strength))
        print("sta: " + str(self.stamina))
        print("perks: " + str(self.perks))
        print("traits: " + str(self.traits))
        print("rituals: " + str(self.rituals))
        print("fertile: " + str(self.fertile))
        print("matur: " + str(self.maturation))
        print("child: " + str(self.child))
        print("parent: " + str(self.parent))
        print("hunger: " + str(self.hunger))
        print("fed: " + str(self.fed))
        print("tree: " + str(self.tree))
        print("inheritance: " + str(self.inheritance))
        print("intel(): " + str(self.g_intel()))
        print("str(): " + str(self.g_strength()))
        print("sta(): " + str(self.g_stamina()))

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

    def g_intel(self):
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
            
    def g_strength(self):
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

    def g_stamina(self):
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

    def add_perk(self, perk_name, perk_dict) -> None:
        self.perks.add(perk_name)
        perk_dict[perk_bame].actions(self)

    def add_ritual(self, ritual_name, rit_dict) -> None:
        self.rituals.add(ritual_name)
        ritual_dict[ritual_name].actions(self)

    def lay_egg(self, new_id, new_name):
        if(self.fertile == True):
            self.fertile = False
            self.child = new_id
            return Cock(new_id,
                        new_name,
                        int(self.g_intel()*self.inheritance),
                        int(self.g_strength()*self.inheritance),
                        int(self.g_stamina()*self.inheritance),
                        parent=self.id)

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
