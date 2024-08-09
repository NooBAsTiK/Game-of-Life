import pygame
import random
from interface import interface_object
import config


screen = screen = pygame.display.set_mode((config.WINDOW_SIZE))
class Triangle(interface_object.InterfaceObject):
    def __init__(self, position, size, color):
        super().__init__()
        self.position = position
        self.size = size
        self.color = color

    def move_away_from_mouse(self, mouse_pos):
        x, y = self.position
        mx, my = mouse_pos

        # Случайный тремор
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1),
                      (1, -1), (1, 1)]
        dx, dy = random.choice(directions)

        # Случайное движение от мышки
        step_size = random.randint(5, 10)
        x += dx * step_size
        y += dy * step_size

        # Запрет на выход границ
        x = max(0, min(x, screen.get_width() - self.size))
        y = max(self.size, min(y, screen.get_height()))

        self.position = (x, y)

    def draw(self, screen):
        x, y = self.position
        points = [(x, y), (x + self.size, y),
                  (x + self.size // 2, y - self.size)]
        pygame.draw.polygon(screen, self.color, points)
