import pygame
from typing import Tuple

from .interface_object import InterfaceObject

Vector2 = Tuple[int, int]
Color = Tuple[int, int, int]


class Label(InterfaceObject):
    _position: Tuple[int, int] = (0, 0)
    _text: str = ""
    _font_size: int = 36
    _color: Tuple[int, int, int] = (0, 0, 0)

    def __init__(self,
                 position: Vector2 | None = None,
                 color: Color | None = None,
                 text: str = ""):

        super().__init__()

        if position:
            self.set_position(position)
        if color:
            self.set_color(color)
        if text:
            self.set_text(text)

        self._font = pygame.font.Font(None, self._font_size)

    def set_position(self, position: Tuple[int, int]):
        self._position = position

    def set_text(self, text: str):
        self._text = text

    def set_color(self, color: Tuple[int, int, int]):
        self._color = color

    def draw(self, screen: pygame.Surface):
        render = self._font.render(self._text, 1, self._color)
        screen.blit(render, self._position)
