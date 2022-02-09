import pygame
from Grain import Grain
from Events import ritual
from Perks import Perks
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
                max_hunger = MAX_HUNGER,
                tree = None,
                inheritance = STAT_INHERITANCE,
                *groups: AbstractGroup,
                perk_dict = {"default perk":Perks(name="default perk")},
                grain_dict = {"default grain":Grain(name="default grain")},
                ritual_dict = {"default ritual":ritual(name="default ritual")}) -> None:
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
        self.max_hunger = max_hunger
        self.fed = {}
        self.tree = tree
        self.inheritance = inheritance
        self.perk_dict = perk_dict
        self.grain_dict = grain_dict
        self.ritual_dict = ritual_dict


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

    def feed(self, grain_name, quantity) -> None:
        grain = self.grain_dict[grain_name]
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
            ritual = self.ritual_dict[rit]
            intel *= ritual.int_mult
            intel += ritual.int_mod
        for perks in self.perks:
            perk = self.perk_dict[perks]
            intel *= perk.int_mult
            intel += perk.int_mod
        return intel
            
    def g_strength(self):
        strength = self.strength
        for rit in self.rituals:
            ritual = self.ritual_dict[rit]
            strength *= ritual.str_mult
            strength += ritual.str_mod
        for perks in self.perks:
            perk = self.perk_dict[perks]
            strength *= perk.str_mult
            strength += perk.str_mod
        return strength

    def g_stamina(self):
        stam = self.stamina
        for rit in self.rituals:
            ritual = self.ritual_dict[rit]
            stam *= ritual.sta_mult
            stam += ritual.sta_mod
        for perks in self.perks:
            perk = self.perk_dict[perks]
            stam *= perk.sta_mult
            stam += perk.sta_mod
        return stam

    def add_perk(self, perk_name) -> None:
        self.perks.add(perk_name)
        self.perk_dict[perk_name].action(self)

    def add_ritual(self, ritual_name) -> None:
        self.rituals.add(ritual_name)
        self.ritual_dict[ritual_name].action(self)

    def lay_egg(self, new_id, new_name, nb_cocks):
        if(self.fertile and nb_cocks < 20):
            self.fertile = False
            self.child = new_id
            return Cock(new_id,
                        new_name,
                        int(self.g_intel()*self.inheritance),
                        int(self.g_strength()*self.inheritance),
                        int(self.g_stamina()*self.inheritance),
                        parent=self.id)
        else:
            print("Conditions infavorables à la ponte")
            return 1

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def draw(self):
        pass
