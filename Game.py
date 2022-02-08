import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.clock = pygame.time.Clock()
        self.HEIGHT = 1024
        self.WIDTH = 768
        self.display = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

    def game_loop(self):
        while self.playing:
            self.check_events()

    def draw_text(self, text, size, x, y, color):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)


    def check_events(self):
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 self.running, self.playing = False, False
