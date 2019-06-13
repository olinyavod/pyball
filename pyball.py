import pygame_sdl2
pygame_sdl2.import_as_pygame()
import os
from game import Game

assert os.path.isfile('sound_effects/brick_hit.wav')


class Pyball(Game):

    def __init__(self):
        Game.__init__(self, 'pyball', 800, 600, 'images/background.jpg', 60)
        pass

Pyball().run()