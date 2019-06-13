import pygame
import sys
from typing import List
from game_object import GameObject


class Game:

    def __init__(self, caption: str, width: int, height:int, backroundFile: str, frameRate: int):
        self.caption = caption
        self.backgroundImage = pygame.image.load(backroundFile)
        self.frameRate = frameRate
        self.gameOver = False
        self.objects = list()
        pygame.mixer.pre_init(44100, 16, 2)
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.mouse_handlers = []

    def update(self) -> None:
        for o in self.objects:
            o.update()

    def draw(self) -> None:
        for o in self.objects:
            o.draw(self.surface)

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def run(self) -> None:
        while not self.gameOver:
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frameRate)