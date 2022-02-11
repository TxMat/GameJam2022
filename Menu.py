import pygame.image

from Button import Button
from Consts import *
from Credits import Credits
from Farm import Farm
from Player import Player
from State import State
from Sun import Sun


class Menu(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.looping = False
        self.player = Player()
        self.backgound_img = pygame.image.load("Assets/menu.png")
        self.bgm()
        self.new_game_btn = Button(self.game, WIDTH / 2, 327, "Jouer", 100)
        self.regles_btn = Button(self.game, WIDTH / 2, 605, "Regles", 80, (112, 112, 112), (158, 158, 158))
        self.credit_btn = Button(self.game, 950, 740, "Credits", 40, (207, 167, 88))
        self.sun = Sun(self.game, (906, 20), 0.9)

    def update(self, dt, actions):
        self.new_game_btn.update(self.game.events)
        self.credit_btn.update(self.game.events)
        self.regles_btn.update(self.game.events)
        self.sun.update(dt)
        if self.new_game_btn.ispressed or actions["ok"]:
            self.game.music_player.music.fadeout(1000)
            new_state = Farm(self.game, self.player)
            new_state.enter_state()
        if self.regles_btn.ispressed:
            new_state = Regles(self.game)
            new_state.enter_state()
        if self.credit_btn.ispressed:
            new_state = Credits(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.backgound_img, (0, 0))
        self.sun.render(display)
        self.new_game_btn.render(display)
        self.credit_btn.render(display)
        self.regles_btn.render(display)

    def bgm(self):
        self.game.music_player.music.load("Assets/first.mp3")
        self.game.music_player.music.play(1)
        self.game.music_player.music.queue("Assets/loopv3.mp3", "", -1)
