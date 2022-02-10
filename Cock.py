import random

import pygame

from Consts import *
from Grain import Grain
from Events import ritual, gen_rituals
from Perks import Perks, gen_perks
from pygame.sprite import AbstractGroup

from Utils import frames_from_spritesheet, scale

perk_dict = gen_perks()
ritual_dict = gen_rituals()
print(ritual_dict.keys())

class Cock(pygame.sprite.Sprite):
    def __init__(self,
                 player = None,
                 id = -1,
                 name = "debug_cock",
                 scalex=1,
                 intelligence=1,
                 strength=1,
                 stamina=1,
                 perks=set(),
                 traits=set(),
                 rituals=set(),
                 fertile=True,
                 maturation=0,
                 child="",
                 parent="",
                 hunger=MAX_HUNGER,
                 max_hunger=MAX_HUNGER,
                 tree=None,
                 inheritance=STAT_INHERITANCE,
                 *groups: AbstractGroup,
                 perk_dict={"default perk": Perks(name="default perk")},
                 grain_dict={"default grain": Grain(name="default grain")},
                 ritual_dict={"default ritual": ritual(name="default ritual")}) -> None:
        super().__init__(*groups)
        self.anim_mode = 0
        self.scale = scalex
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
        self.curr_frame, self.last_frame_update = 0, 0
        self.walk_frame_list = frames_from_spritesheet("Assets/cock_walk.png", 0, 0, 48, 48, 6)
        self.idle_frame_list = frames_from_spritesheet("Assets/cock_idle.png", 0, 0, 48, 48, 6)
        self.run_frame_list = frames_from_spritesheet("Assets/cock_run.png", 0, 0, 48, 48, 2)
        self.curr_frame_list = self.idle_frame_list
        self.frame_to_show = scale(self.idle_frame_list[0], self.scale)
        self.frame_to_show_hover = scale(self.frame_to_show, 1)
        self.cock_rect = self.frame_to_show.get_rect()
        self.ispressed = False
        self.isvalidspawn = False
        self.curr_y = None
        self.curr_x = None
        colided_count = 0

        def spawn_box():
            self.curr_y = random.randint(390, 560)
            tmp = int(135 / 102 * (self.curr_y - 420))
            self.curr_x = random.randint(260 - tmp, 580 - tmp)
            self.cock_rect.center = (self.curr_x + 24, self.curr_y + 24)

        while not self.isvalidspawn and player:
            spawn_box()
            collided = False
            for cocks in player.cocks.values():
                if self.cock_rect.colliderect(cocks.cock_rect):
                    collided = True
                    colided_count += 1  # removes soft lock
            if not collided or colided_count > 100000:
                self.isvalidspawn = True

        self.image = pygame.Surface((40, 40))
        self.image.fill((200, 30, 30))
        self.rect = self.image.get_rect(center=(400, 400))
        self.current_health = 0
        self.target_health = MAX_HUNGER * 10
        self.max_health = MAX_HUNGER * 10
        self.health_bar_length = 50
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change_speed = 5
        self.display_health_bar = True

    def loose_hunger(self, amount):
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health < 0:
            self.target_health = 0

    def get_hunger(self, amount):
        if self.target_health < self.max_health:
            self.target_health += amount
        if self.target_health > self.max_health:
            self.target_health = self.max_health

    def advanced_health(self, display):
        transition_width = 0
        transition_color = (255, 0, 0)

        if self.current_health < self.target_health:
            self.current_health += self.health_change_speed
            transition_width = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (0, 0, 0)

        if self.current_health > self.target_health:
            self.current_health -= self.health_change_speed
            transition_width = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (255, 255, 0)

        health_bar_width = int(self.current_health / self.health_ratio)
        health_bar = pygame.Rect(self.curr_x, self.curr_y, health_bar_width, 3)
        transition_bar = pygame.Rect(health_bar.right, self.curr_y, transition_width, 3)

        pygame.draw.rect(display, (230, 230, 100), health_bar)
        pygame.draw.rect(display, transition_color, transition_bar)

    def info_cock(self):
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
        self.hunger += grain.hunger * quantity
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
            intel += perk.int_mod
        return int(intel)

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
        return int(strength)

    def g_stamina(self):
        stam = self.stamina
        for rit in self.rituals:
            ritual = ritual_dict[rit]
            stam *= ritual.sta_mult
            stam += ritual.sta_mod
        for perks in self.perks:
            perk = perk_dict[perks]
            stam *= perk.sta_mult
            stam += perk.sta_mod
        return int(stam)

    def add_perk(self, perk_name) -> None:
        self.perks.add(perk_name)
        #perk_dict[perk_name].action(self)

    def add_ritual(self, ritual_name) -> None:
        self.rituals.add(ritual_name)
        #ritual_dict[ritual_name].action(self)

    def lay_egg(self, new_id=0, new_name="", nb_cocks=1):
        if self.fertile and nb_cocks < MAX_COCKS:
            self.fertile = False
            self.child = new_name
            return Cock(new_id,
                        new_name,
                        int(self.g_intel() * self.inheritance),
                        int(self.g_strength() * self.inheritance),
                        int(self.g_stamina() * self.inheritance),
                        parent=self.name)
        else:
            print("Conditions infavorables à la ponte")
            return 1

    def update(self, delta_time, events):
        self.animate(delta_time)
        # self.cock_rect = self.frame_to_show.get_rect()
        # self.cock_rect.center = (self.curr_x, self.curr_y)
        hover = self.cock_rect.collidepoint(pygame.mouse.get_pos())
        self.ispressed = False
        # if hover:
        #    self.frame_to_show = self.frame_to_show_hover later
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and hover:
                self.ispressed = True
                print("clicked") # debug

    def animate(self, delta_time):
        if self.anim_mode == 0:
            self.curr_frame_list = self.idle_frame_list
        elif self.anim_mode == 1:
            self.curr_frame_list = self.walk_frame_list
        elif self.anim_mode == 2:
            self.curr_frame_list = self.run_frame_list
        self.last_frame_update += delta_time
        if self.last_frame_update > .15:
            self.curr_frame = (self.curr_frame + 1) % len(self.curr_frame_list)
            self.frame_to_show = self.curr_frame_list[self.curr_frame]
            self.frame_to_show = scale(self.frame_to_show, self.scale)
            self.last_frame_update = 0

    def render(self, surface):
        if self.display_health_bar:
            self.advanced_health(surface)
        surface.blit(self.frame_to_show, (self.curr_x, self.curr_y))
