import pygame

class TextObject:
	
	def __init__(self, x: int, y: int, text_func, color, font_name: str, font_size: float):
		self.pos = (x,y)
		self.text_func = text_func
		self.color = color
		self.font = pygme.font.SysFont(font_name, font_size)