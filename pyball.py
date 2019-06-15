import os
import platform
print(platform.system())
if platform.system() == 'Linux':
	import pygame_sdl2
	pygame_sdl2.import_as_pygame()

from game import Game
from background import Background

assert os.path.isfile('sound_effects/brick_hit.wav')


class Pyball(Game):

	def __init__(self):
		Game.__init__(self, 'pyball', 1000, 600, 60)
		sw, sh = self.surface.get_size()
		self.objects.insert(0, Background(sw, sh))
        
def main():
	Pyball().run()
	
if __name__ == '__main__':
	main()