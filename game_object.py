from pygame.rect import Rect

class GameObject:
	
	def __init__(self, x: int, y: int, width: int, height: int, speed = (0, 0)):
		self.bounds = Rect(x, y, width, height)
		self.speed = speed
	
	@property
	def left(self):
		return self.bounds.left

	@property
	def right(self):
		return self.bounds.right

	@property
	def width(self):
		return self.bounds.width

	@property
	def height(self):
		return self.bounds.height

	@property
	def top(self):
		return self.bounds.top

	@property
	def bottom(self):
		return self.bounds.bottom

	@property
	def center(self):
		return self.bounds.center

	@property
	def centerx(self):
		return self.bounds.centerx

	@property
	def centery(self):
		return self.bounds.centery

	def draw(self, surface) -> None:
		pass

	def move(self, dx, dy) -> None:
		self.bounds = self.bounds.move(dx, dy)
		
	def update(self) -> None:
		if self.speed == [0, 0]:
			return
		
		self.move(*self.speed)
