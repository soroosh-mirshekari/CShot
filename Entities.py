# entities.py
from abc import ABC, abstractmethod
import pygame
from random import randint

# an Instanst
class Entity(ABC):
    @abstractmethod
    def __init__(self, border_thickness, width, height, screen):
        self._border_thickness = border_thickness
        self._width = width
        self._height = height
        self._screen = screen

    @abstractmethod
    def random_placement(self):
        pass

class Aim(Entity):
    def __init__(self, border_thickness, width, height, screen, speed, size, color, controls):
        super().__init__(border_thickness, width, height, screen)
        self.__speed = speed
        self.__size = size
        self.__color = color
        self.__controls = controls
        self.__x = randint(border_thickness, width - border_thickness)
        self.__y = randint(border_thickness, height - border_thickness)

    def random_placement(self):
        self.__x = randint(self._border_thickness, self._width - self._border_thickness)
        self.__y = randint(self._border_thickness, self._height - self._border_thickness)

    def press_key(self, keys):

        # Move aim based on WASD keys
        if keys[self.__controls[0]]:  # Up
            self.__y -= self.__speed
        if keys[self.__controls[1]]:  # Down
            self.__y += self.__speed
        if keys[self.__controls[2]]:  # Left
            self.__x -= self.__speed
        if keys[self.__controls[3]]:  # Right
            self.__x += self.__speed

        # Keep aim within screen bounds
        self.__x = max(self._border_thickness, min(self.__x, self._width - self._border_thickness))
        self.__y = max(self._border_thickness, min(self.__y, self._height - self._border_thickness))

    def draw(self):  # Draw aim
        pygame.draw.circle(self._screen, self.__color, (int(self.__x), int(self.__y)), self.__size)

        # Update the display
        pygame.display.flip()