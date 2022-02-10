from Player import Player
from State import State
from Farm import Farm


class Menu(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.looping = False
        self.player = Player()
        self.bgm()

    def update(self, dt, actions):
        if actions["ok"]:
            new_state = Farm(self.game, self.player)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((60, 60, 60))
        self.game.draw_text(display, "coucou", 100, 500, 200, (180, 180, 180))

    def bgm(self):
        self.game.music_player.music.load("Assets/first.mp3")
        self.game.music_player.music.play(1)
        self.game.music_player.music.queue("Assets/loopv3.mp3", "", -1)
