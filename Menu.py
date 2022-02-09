from State import State
from Farm import Farm


class Menu(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self, dt, actions):
        if actions["ok"]:
            new_state = Farm(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((60, 60, 60))
        self.game.draw_text(display, "coucou", 100, 500, 200, (180, 180, 180))
