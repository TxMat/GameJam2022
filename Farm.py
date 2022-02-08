import pygame
from State import State
from Utils import *


class Farm(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.isNight = False
        self.HUD = HUD(self.game)
        self.background_img = pygame.image.load("Assets/backgound_day.png").convert()
        self.sun = Sun(self.game)

    def update(self, delta_time, actions):
        self.sun.update(delta_time)

    def render(self, surface):
        surface.blit(self.background_img, (0, 0))
        self.sun.render(surface)


class Sun():
    def __init__(self, game):
        self.game = game
        self.curr_frame, self.last_frame_update = 0, 0
        self.frame_list = frames_from_spritesheet("Assets/sun.png", 0, 0, 94, 94, 2)
        self.frame_to_show = scale(self.frame_list[0], 0.9)

    def update(self, delta_time):
        self.animate(delta_time)

    def render(self, surface):
        surface.blit(self.frame_to_show, (900, 30))

    def animate(self, delta_time):
        self.last_frame_update += delta_time
        if self.last_frame_update > 1:
            self.curr_frame = (self.curr_frame + 1) % len(self.frame_list)
            self.frame_to_show = self.frame_list[self.curr_frame]
            self.frame_to_show = scale(self.frame_to_show, 0.9)
            self.last_frame_update = 0


class HUD:
    def __init__(self, game):
        self.plyr_name = ""
        self.day = 1
        self.money = 0
        self.cock_number = 0
        # btn invoke
        # btn cocks
        # btn last expedition

    def update(self):
        pass

    def render(self, surface):
        pass
