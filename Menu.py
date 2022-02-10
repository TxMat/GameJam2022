from Button import Button
from Consts import *
from Player import Player
from State import State
from Farm import Farm
from Credits import Credits


class Menu(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.looping = False
        self.player = Player()
        self.bgm()
        self.new_game_btn = Button(self.game, WIDTH / 2, 350, "New Game", 100)
        self.credit_btn = Button(self.game, WIDTH / 2, 500, "Credits", 100)

    def update(self, dt, actions):
        self.new_game_btn.update(self.game.events)
        self.credit_btn.update(self.game.events)
        if self.new_game_btn.ispressed or actions["ok"]:
            self.game.music_player.music.fadeout(4000)
            new_state = Farm(self.game, self.player)
            new_state.enter_state()
        if self.credit_btn.ispressed:
            new_state = Credits(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((60, 60, 60))
        self.game.draw_text(display, "Cock Digger", 150, WIDTH/2, 80, (180, 180, 180))
        self.new_game_btn.render(display)
        self.credit_btn.render(display)

    def bgm(self):
        self.game.music_player.music.load("Assets/first.mp3")
        self.game.music_player.music.play(1)
        self.game.music_player.music.queue("Assets/loopv3.mp3", "", -1)
