import pygame
from game_object import GameObject
from typing import Iterator
import random

class Star(GameObject):
	def __init__(self, x: int, y: int, size: int, speed, backgroundWidth: int, backgroundHeight: int):
		GameObject.__init__(self, x, y, size, size, speed)
		self.backgroundWidth = backgroundWidth
		self.backgroundHeight = backgroundHeight
		self.actualTop = self.top
		self.actualLeft = self.left
		
	def draw(self, surface):
		pygame.draw.circle(surface, (255, 255, 255), self.center, self.width/2)
		
	def update(self):
		dx, dy = self.speed
		self.actualTop += dy
		self.actualLeft += dx
		
		self.bounds.top = self.actualTop
		self.bounds.left = self.actualLeft
		
		if self.top > self.backgroundHeight or self.left > self.backgroundHeight:
			self.actualLeft = random.randint(0, self.backgroundWidth)
			self.actualTop = random.randint(-200, 0)

class Background(GameObject):
	
	def __init__(self, width: int, height: int):
		GameObject.__init__(self, 0, 0, width, height, (0,0))
		self.stars = list(self.genStars())
	
	def genStars(self) -> Iterator[Star]:
		for i in range(30):
			yield Star(random.randint(0, self.width), random.randint(0, self.height), 3, (0, 0.5), self.width, self.height)
			
		for i in range(30):
			yield Star(random.randint(0, self.width), random.randint(0, self.height), 2, (0, .3), self.width, self.height)
			
		for i in range(30):
			yield Star(random.randint(0, self.width), random.randint(0, self.height), 1, (0, 0.1), self.width, self.height)	
	
	def update(self):
		for s in self.stars:
			s.update()
				
	def draw(self, surface):
		surface.fill((0, 0, 0))
		
		for s in self.stars:
			s.draw(surface)
		
