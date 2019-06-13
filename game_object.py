from pygame.rect import Rect
from typing import Tuple


class GameObject:

    def __init__(self, x: float, y: float, width: float, height: float, speed: Tuple[float, float] = (0, 0)):
        self.bounds = Rect(x, y, width, height)
        self.speed = speed

    @property
    def left(self) -> float:
        return self.bounds.left

    @property
    def right(self) -> float:
        return self.bounds.right

    @property
    def width(self) -> float:
        return self.bounds.width

    @property
    def height(self) -> float:
        return self.bounds.height

    @property
    def top(self) -> float:
        return self.bounds.top

    @property
    def bottom(self) -> float:
        return self.bounds.bottom

    @property
    def center(self) -> Tuple[float, float]:
        return self.bounds.center

    @property
    def centerx(self) -> float:
        return self.bounds.centerx

    @property
    def centery(self) -> float:
        return self.bounds.centery

    def draw(self, surface) -> None:
        pass

    def move(self, dx, dy) -> None:
        self.bounds = self.bounds.move(dx, dy)

    def update(self) -> None:
        if self.speed == [0, 0]:
            return

        self.move(*self.speed)
