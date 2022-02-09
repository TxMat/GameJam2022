from multiprocessing.connection import wait
import this
import time
import pygame

from Menu import Menu
from Farm import Farm
from Expedition import Expedition


class Game:
    def __init__(self):
        self.title_screen = None
        pygame.init()
        self.running, self.playing = True, True
        self.clock = pygame.time.Clock()
        self.WIDTH = 1024
        self.HEIGHT = 768
        self.display = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.font_loc = "Assets/font.ttf"
        self.state_stack = []
        self.dt, self.prev_time = 0, 0
        self.actions = {"left": False, "right": False, "up": False, "down": False, "ok": False}
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.events = None
        self.load_states()

    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.check_events()
            self.update()
            self.draw()

    def draw_text(self, surface, text, size, x, y, color=(200, 200, 200)):
        font = pygame.font.Font(self.font_loc, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def check_events(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.actions["down"] = True
                if event.key == pygame.K_UP:
                    self.actions["up"] = True
                if event.key == pygame.K_LEFT:
                    self.actions["left"] = True
                if event.key == pygame.K_RIGHT:
                    self.actions["right"] = True
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.actions["ok"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.actions["down"] = False
                if event.key == pygame.K_UP:
                    self.actions["up"] = False
                if event.key == pygame.K_LEFT:
                    self.actions["left"] = False
                if event.key == pygame.K_RIGHT:
                    self.actions["right"] = False
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.actions["ok"] = False

    def load_states(self):
        self.title_screen = Menu(self)
        self.state_stack.append(self.title_screen)

    def update(self):
        self.state_stack[-1].update(self.dt, self.actions)

    def draw(self):
        self.state_stack[-1].render(self.display)
        # Render current state to the screen
        self.screen.blit(pygame.transform.scale(self.display, (self.WIDTH, self.HEIGHT)), (0, 0))
        pygame.display.flip()

    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False
