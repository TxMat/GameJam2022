from State import State


class Credits(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.looping = False

    def update(self, dt, actions):
        if actions["ok"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((60, 60, 60))
        self.game.draw_text(display, "Fait Par: Elsa BERNET, Quentin CARREL, Mathieu PONAL, Emmanuel ARNOUX-BONKOWSKI",
                            20, 500, 100, (180, 180, 180))
        self.game.draw_text(display,
                            "Musique: Game-of-role - opening s5, T.E.S.5 - around the fire, the witcher3 - the nightingales",
                            20, 500, 120, (180, 180, 180))
        self.game.draw_text(display, "Sprite: Nolla games - noita ", 20, 500, 140, (180, 180, 180))
