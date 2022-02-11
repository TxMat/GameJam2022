from Utils import frames_from_spritesheet, scale


class Sun:
    def __init__(self, game, pos, scalex):
        self.game = game
        self.scale = scalex
        self.pos = pos
        self.curr_frame, self.last_frame_update = 0, 0
        self.frame_list = frames_from_spritesheet("Assets/sun.png", 0, 0, 94, 94, 2)
        self.frame_to_show = scale(self.frame_list[0], self.scale)

    def update(self, delta_time):
        self.animate(delta_time)

    def render(self, surface):
        surface.blit(self.frame_to_show, self.pos)

    def animate(self, delta_time):
        self.last_frame_update += delta_time
        if self.last_frame_update > 1:
            self.curr_frame = (self.curr_frame + 1) % len(self.frame_list)
            self.frame_to_show = self.frame_list[self.curr_frame]
            self.frame_to_show = scale(self.frame_to_show, self.scale)
            self.last_frame_update = 0
